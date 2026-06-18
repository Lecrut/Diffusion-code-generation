import hashlib
from datetime import datetime
class SecureLogger:
    def __init__(self):
        self.decision_log = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        hashed_data = hashlib.sha256(f"{user_id}:{decision_type}".encode()).hexdigest()
        log_entry = {
            "timestamp": timestamp,
            "hashed_input": hashed_data,
            "status": "logged"
        }
        self.decision_log.append(log_entry)
if __name__ == '__main__':
    logger = SecureLogger()
    user_id_1 = 1001
    decision_type_1 = "approve_transaction"
    user_id_2 = 1002
    decision_type_2 = "reject_access"
    logger.log_decision(user_id=user_id_1, decision_type=decision_type_1)
    logger.log_decision(user_id=user_id_2, decision_type=decision_type_2)