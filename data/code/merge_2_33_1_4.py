import sqlite3
def check_username(username: str) -> bool:
    db_sources = [
        ("users", "SELECT 1 FROM users WHERE LOWER(name) = ?"),
        ("accounts", "SELECT 1 FROM accounts WHERE LOWER(account_name) = ?"),
        ("memberships", "SELECT 1 FROM memberships WHERE LOWER(member_id) = ?"),
    ]
    for table, query in db_sources:
        try:
            conn = sqlite3.connect(f"database_{table}.db")
            cursor = conn.cursor()
            cursor.execute(query.lower(), [username])
            if cursor.fetchone():
                return True
            conn.close()
        except Exception as e:
            print(f"Error checking {table}: {e}")
    return False
if __name__ == '__main__':
    test_user = "john_doe"
    result = check_username(test_user)
    if result:
        print("Username exists.")
    else:
        print("Username not found.")