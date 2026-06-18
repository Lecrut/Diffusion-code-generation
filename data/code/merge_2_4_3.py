import hashlib
from datetime import datetime
class SecureLogger:
    def __init__(self):
        self.decisions = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        hashed_data = hashlib.sha256(f"{user_id}:{decision_type}".encode()).hexdigest()
        entry = {
            "timestamp": timestamp,
            "hashed_input": hashed_data,
            "status": "logged"
        }
        self.decisions.append(entry)
    def get_summary(self):
        return len(self.decisions), [d["timestamp"] for d in self.decisions]
if __name__ == '__main__':
    logger = SecureLogger()
    logger.log_decision(user_id="user_123", decision_type="access_granted")
    logger.log_decision(user_id="user_456", decision_type="denied")
    count, timestamps = logger.get_summary()
    print(f"Total decisions logged: {count}")