from flask import Flask, request, render_template
from conf.settings import db_config
import pymysql

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    if request.method == 'POST':
        content = request.form['content']
        sql_insert = "INSERT INTO messages (text) VALUES (%s);"
        cursor.execute(sql_insert, (content,))
        conn.commit()

    sql_select = "SELECT * FROM messages;"
    cursor.execute(sql_select)
    messages = cursor.fetchall()
    print(messages)
    cursor.close()
    conn.close()

    return render_template('index.html', messages=messages)
