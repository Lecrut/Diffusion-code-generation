import sqlite3
class UserDatabaseManager:
    def __init__(self):
        self.connection = None
    def connect(self, db_name="users.db"):
        try:
            self.connection = sqlite3.connect(db_name)
            cursor = self.connection.cursor()
            cursor.execute()
            self.connection.commit()
        except Exception as e:
            print(f"Database connection error: {e}")
    def verify_username(self, target_name):
        if not self.connection or not hasattr(self.connection, 'cursor'):
            return False
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id FROM users WHERE username=?", (target_name,))
            result = cursor.fetchone()
            return bool(result)
        except sqlite3.Error as e:
            print(f"Verification error: {e}")
            return False
    def close(self):
        if self.connection:
            self.connection.close()
if __name__ == '__main__':
    manager = UserDatabaseManager()
    manager.connect("sample_users.db")
    test_names = ["alice", "bob", "charlie"]
    results = [manager.verify_username(name) for name in test_names]
    print(f"Verification Results: {results}")
    manager.close()