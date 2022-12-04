from urllib.parse import urlparse
import os
import psycopg2


def main(args):
    print("hello from hello")
    db_url = os.environ.get("DATABASE_URL")
    assert db_url is not None, "DATABASE_URL is missing!"
    print("db_url found")
    p = urlparse(db_url)
    print("parsed")
    conn = psycopg2.connect(
        dbname="defaultdb",
        user=p.username,
        password=p.password,
        port=p.port,
        host=p.hostname,
        sslmode="require",
    )
    print("connection created")
    conn.close()
    print("connection closed")
    return {"body": str(44)}