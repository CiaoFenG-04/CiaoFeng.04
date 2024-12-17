import psycopg2

__cnx = None

def get_sql_connection():
    global __cnx
    try:
        if not __cnx or __cnx.closed:
            __cnx = psycopg2.connect(
                host="localhost",
                database="postgres",
                user="postgres",
                password="2807"
            )
        return __cnx
    except Exception as e:
        print(f"Error connecting to database: {str(e)}")