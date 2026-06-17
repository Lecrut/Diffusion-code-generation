import sqlite3
def check_username(username: str) -> bool:
    sources = [
        ("users", "SELECT 1 FROM users WHERE LOWER(name) = ?"),
        ("accounts", "SELECT 1 FROM accounts WHERE LOWER(login_name) = ?"),
        ("members", "SELECT 1 FROM members WHERE LOWER(member_id) = ?"),
    ]
    for table, query in sources:
        try:
            with sqlite3.connect("database.db") as conn:
                cursor = conn.cursor()
                result = cursor.execute(query.lower(), [username]).fetchone()
                if result is not None:
                    return True
        except Exception:
            continue
    return False
if __name__ == '__main__':
    test_usernames = ["alice", "bob123", "charlie"]
    for user in test_usernames:
        exists = check_username(user)
        print(f"Username '{user}' exists: {exists}")