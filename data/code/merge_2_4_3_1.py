import hashlib
from datetime import datetime
class SecureLogger:
    def __init__(self):
        self.decisions = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        hashed_input = hashlib.sha256(f"{user_id}:{decision_type}".encode()).hexdigest()
        log_entry = {
            "timestamp": timestamp,
            "hashed_user_decision": hashed_input,
            "status": "logged"
        }
        self.decisions.append(log_entry)
if __name__ == '__main__':
    logger = SecureLogger()
    user_id_1 = 1001
    decision_type_1 = "approve_transaction"
    user_id_2 = 1002
    decision_type_2 = "deny_access"
    logger.log_decision(user_id_1, decision_type_1)
    logger.log_decision(user_id_2, decision_type_2)