from flask import Flask, request, jsonify
#import redis

app = Flask(__name__)

# 连接到本地 Redis 服务器
#redis_client = redis.Redis(host='localhost', port=6379, db=0, password="3558hominT.")
db_data = []

@app.route('/push', methods=['POST'])
def push_message():
    data = request.get_json()
    message = data.get('message')
    if message:
        db_data.append(message)
        # 使用 LPUSH 将消息推送到名为 "messages" 的 Redis 列表
        #redis_client.lpush('messages', message)
        return jsonify({'status': 'success', 'message': 'Message pushed'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'No message provided'}), 400

@app.route('/pull', methods=['GET'])
def pull_message():
    # 使用 RPOP 从名为 "messages" 的 Redis 列表中拉取最早的消息
    # message = redis_client.rpop('messages')
    if db_data != []:
        return jsonify({'status': 'success', 'message': db_data}), 200
    else:
        return jsonify({'status': 'success', 'message': 'No messages left'}), 200

if __name__ == '__main__':
    app.run(debug=True)
