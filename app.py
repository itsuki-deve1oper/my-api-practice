# 例：Flaskを使う場合
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Render!"

if __name__ == "__main__":
    # Renderが指定するポート番号を読み込む（超重要！）
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
