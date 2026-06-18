import sqlite3
def check_username(username: str) -> bool:
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = "SELECT 1 FROM users WHERE LOWER(name) = ?"
        cursor.execute(query, (username.lower(),))
        result = cursor.fetchone()
        if result is not None:
            return True
    except Exception as e:
        print(f"Database error for {username}: {e}")
    finally:
        conn.close()
    return False
def check_username_secondary(username: str) -> bool:
    try:
        conn = sqlite3.connect("users_backup.db")
        cursor = conn.cursor()
        query = "SELECT 1 FROM users WHERE LOWER(name) = ?"
        cursor.execute(query, (username.lower(),))
        result = cursor.fetchone()
        if result is not None:
            return True
    except Exception as e:
        print(f"Secondary database error for {username}: {e}")
    finally:
        conn.close()
    return False
def check_username_ternary(username: str) -> bool:
    try:
        with open("users.txt", "r") as f:
            lines = [line.strip().lower() for line in f.readlines()]
            return any(line == username.lower() for line in lines)
    except FileNotFoundError:
        print(f"File not found for {username}")
        return False
    except Exception as e:
        print(f"Tertiary data source error for {username}: {e}")
    return False
def verify_username(username: str, primary_db: bool = True, secondary_db: bool = True) -> tuple[bool, list[str]]:
    results = []
    if primary_db and check_username(username):
        results.append("Primary DB")
    elif not primary_db or check_username_secondary(username):
        results.append("Secondary DB")
    return len(results) > 0, results
if __name__ == '__main__':
    test_usernames = ["alice", "bob123", "charlie"]
    for user in test_usernames:
        exists, sources = verify_username(user)
        print(f"User {user}: {'Exists' if exists else 'Not found'} via {', '.join(sources)}")