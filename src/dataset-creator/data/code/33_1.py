import sqlite3
def check_username(username: str) -> bool:
    sources = ['users', 'members']
    for db_name in sources:
        try:
            conn = sqlite3.connect(f'db_{db_name}.sqlite')
            cursor = conn.cursor()
            query = f"SELECT EXISTS(SELECT 1 FROM {db_name} WHERE username = ?)"
            cursor.execute(query, (username,))
            result = cursor.fetchone()[0]
            if result:
                return True
            conn.close()
        except sqlite3.Error as e:
            print(f"Database error in {db_name}: {e}")
    return False
if __name__ == '__main__':
    test_usernames = ['alice', 'bob_invalid']
    for user in test_usernames:
        exists = check_username(user)
        if exists:
            print(f"Username '{user}' found.")
        else:
            print(f"Username '{user}' not found.")