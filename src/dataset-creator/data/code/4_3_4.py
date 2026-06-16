import hashlib
from datetime import datetime
class SecureDecisionLogger:
    def __init__(self):
        self.decisions = []
    def log_decision(self, user_id: str, decision_type: str) -> None:
        timestamp = datetime.now().isoformat()
        combined_data = f"{timestamp}:{user_id}:{decision_type}"
        hash_value = hashlib.sha256(combined_data.encode()).hexdigest()
        self.decisions.append({
            "id": len(self.decisions),
            "hash": hash_value,
            "type": decision_type.upper(),
            "recorded_at": timestamp
        })
    def get_summary(self) -> dict:
        return {
            "total_records": len(self.decisions),
            "unique_decisions": list(set(d["type"] for d in self.decisions)),
            "last_entry_time": self.decisions[-1]["recorded_at"] if self.decisions else None
        }
if __name__ == '__main__':
    logger = SecureDecisionLogger()
    test_cases = [
        ("user_001", "approve"),
        ("user_002", "reject"),
        ("user_003", "pending")
    ]
    for user_id, decision in test_cases:
        logger.log_decision(user_id, decision)
    summary = logger.get_summary()
    print(f"Total Decisions Logged: {summary['total_records']}")
    for record in summary["unique_decisions"]:
        print(record)