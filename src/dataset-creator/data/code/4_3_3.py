import hashlib
from datetime import datetime
import json
import os
class SecureLogger:
    def __init__(self):
        self.logs = []
    def log_decision(self, user_id, decision_type, timestamp=None):
        if timestamp is None:
            timestamp = datetime.now().isoformat()
        safe_user_data = hashlib.sha256(f"{user_id}:{timestamp}".encode()).hexdigest()[:16]
        log_entry = {
            "id": len(self.logs) + 1,
            "type": decision_type,
            "safe_identifier": safe_user_data,
            "recorded_at": timestamp
        }
        self.logs.append(log_entry)
    def get_summary(self):
        return json.dumps({
            "total_entries": len(self.logs),
            "sample_types": list(set([log["type"] for log in self.logs]))
        })
if __name__ == '__main__':
    logger = SecureLogger()
    logger.log_decision(user_id="user_123", decision_type="access_granted")
    logger.log_decision(user_id="admin_user", decision_type="configuration_change")
    summary_data = logger.get_summary()
    print(summary_data)