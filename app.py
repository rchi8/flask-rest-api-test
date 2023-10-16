from flask import Flask, request, jsonify

app = Flask(__name__)
#app.config['JSON_AS_ASCII'] = True

# サンプルデータ（仮のデータベース）
data = {
    "1": {"name": "アイテム１", "description": "これはアイテム１です"},
    "2": {"name": "アイテム2", "description": "これはアイテム2です"},
    # 追加データはここに追加
}

# GETリクエストですべてのデータを取得
@app.route('/api/data/', methods=['GET'])
def get_all_data():
    return jsonify(data)    # dect を json に変換

# GETリクエストで特定のデータを取得
@app.route('/api/data/<data_id>', methods=['GET'])    # <val> で変数へ代入
def get_data(data_id):
    if data_id in data:
        return jsonify(data[data_id])
    else:
        return jsonify({"error": "データが見つかりません"}), 404
    
# POSTリクエストで新しいデータを作成
# データベースを利用してないのでサーバ再起動で消える
@app.route('/api/data/', methods=['POST'])
def create_data():
    new_data = request.get_json()
    data_id = str(len(data) + 1)    # 本来は一意のIDを生成すべき
    data[data_id] = new_data 
    return jsonify({"message": "データが作成されました", "data_id": data_id}), 201


# PUTリクエストでデータを更新
@app.route('/api/data/<data_id>', methods=['PUT'])
def update_data(data_id):
    if data_id in data:
        update_data = request.get_json()
        data[data_id] = update_data
        return jsonify({"message": "データが更新されました", "data_id": data_id})
    else:
        return jsonify({"error": "データが見つかりません"}), 404
    

# DELETEリクエストでデータを削除
@app.route('/api/data/<data_id>', methods=['DELETE'])
def delete_data(data_id):
    if data_id in data:
        del data[data_id]
        return jsonify({"message": "データが削除されました", "data_id": data_id}), 204
    else:
        return jsonify({"error": "データが見つかりません"})

#if __name__ == '__main__':
#    app.run(debug=True)

# 外部アクセス可能にする
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080) 
     # 0.0.0.0ホストと8080ポート#で実行

