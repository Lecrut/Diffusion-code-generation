import hashlib
from datetime import datetime
class SecureLogger:
    def __init__(self):
        self.log_entries = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        hashed_data = hashlib.sha256(f"{user_id}:{decision_type}".encode()).hexdigest()
        entry = {
            "timestamp": timestamp,
            "hashed_input": hashed_data,
            "status": "logged"
        }
        self.log_entries.append(entry)
        return True
if __name__ == '__main__':
    logger = SecureLogger()
    test_cases = [
        {"user_id": 1001, "decision_type": "ACCESS_GRANTED"},
        {"user_id": 1002, "decision_type": "ACCESS_DENIED"},
        {"user_id": 1003, "decision_type": "SESSION_EXPIRED"}
    ]
    for case in test_cases:
        logger.log_decision(**case)