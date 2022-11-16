from flask import Flask
from flask import request, jsonify
import os
import base64

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/photo', methods=["POST"])
def get_data():
    # 接收图片
    upload_file = request.files['file']
    # 获取图片名
    file_name = upload_file.filename
    # 文件保存目录（桌面）
    file_path = r'./receive/'
    if upload_file:
        # 地址拼接
        file_paths = os.path.join(file_path, file_name)
        # 保存接收的图片到桌面
        upload_file.save(file_paths)
        # 随便打开一张其他图片作为结果返回，
        with open(r'./res/images (1).png', 'rb') as f:
            res = base64.b64encode(f.read())
            return res





if __name__ == '__main__':
    app.run()
