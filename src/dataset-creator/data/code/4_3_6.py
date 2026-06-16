import hashlib
from datetime import datetime
class SecureLogger:
    def __init__(self):
        self.log_entries = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        hashed_input = hashlib.sha256(f"{user_id}{decision_type}".encode()).hexdigest()
        log_entry = {
            "timestamp": timestamp,
            "hashed_user_decision": hashed_input,
            "status": "logged"
        }
        self.log_entries.append(log_entry)
        return True
if __name__ == '__main__':
    logger = SecureLogger()
    sample_users = ["user_001", "admin_user"]
    sample_decisions = ["approve_access", "reject_request"]
    for user in sample_users:
        for decision in sample_decisions:
            result = logger.log_decision(user, decision)
            if result:
                print(f"Logged {decision} for {user}")