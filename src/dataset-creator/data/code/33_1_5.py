import sqlite3
def check_username(username: str) -> bool:
    databases = [
        {"name": "users_db", "connection_string": ":memory:"},                         
    ]
    try:
        conn = sqlite3.connect(databases[0]["connection_string"])
        cursor = conn.cursor()
        cursor.execute()
        sample_users = ["alice", "bob"]
        for user in sample_users:
            try:
                cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?)", (user, f"{user}@example.com"))
            except sqlite3.Error as e:
                print(f"Error inserting {user}: {e}")
        conn.commit()
        try:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
            count_in_db = cursor.fetchone()[0]
            if count_in_db > 0:
                return True
            print(f"Username '{username}' not found in local database.")
        except sqlite3.Error as e:
            print(f"Error checking username in {databases[0]['name']}: {e}")
    except Exception as e:
        print(f"Unexpected error during check: {e}")
    return False
if __name__ == '__main__':
    test_usernames = ["alice", "charlie", "bob"]
    for user in test_usernames:
        exists = check_username(user)
        status = "Exists" if exists else "Does not exist"
        print(f"{user}: {status}")