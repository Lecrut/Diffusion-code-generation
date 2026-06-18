import sys
from datetime import datetime
class HierarchicalDecisionEngine:
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    def process_request(self, user_id, request_type, priority_level):
        self.log(f"Processing request for User ID: {user_id}, Type: {request_type}, Priority: {priority_level}")
        if not isinstance(user_id, int) or user_id <= 0:
            self.log("Error: Invalid user ID")
            return {"status": "error", "message": "Invalid user identifier"}
        if request_type not in ["support", "billing", "technical"]:
            self.log(f"Warning: Unknown request type '{request_type}' for User {user_id}")
            return {"status": "warning", "message": f"Request type '{request_type}' is unrecognized but being processed with default logic"}
        if priority_level not in ["high", "medium", "low"]:
            self.log(f"Warning: Unknown priority level '{priority_level}' for User {user_id}")
            return {"status": "warning", "message": f"Priority level '{priority_level}' is unrecognized but being processed with default logic"}
        if request_type == "support" and priority_level in ["high"]:
            self.log(f"High-priority support ticket created for User {user_id}. Escalating to senior team.")
            return {"status": "success", "action": "escalated_support", "details": f"Ticket escalated for user {user_id}"}
        elif request_type == "billing" and priority_level in ["high"]:
            self.log(f"High-priority billing issue detected for User {user_id}. Contacting finance immediately.")
            return {"status": "success", "action": "finance_alert", "details": f"Billing alert sent to user {user_id}"}
        elif request_type == "technical" and priority_level in ["high"]:
            self.log(f"High-priority technical issue reported by User {user_id}. Dispatching IT specialist.")
            return {"status": "success", "action": "it_dispatch", "details": f"IT specialist assigned to user {user_id}"}
        elif request_type == "support" and priority_level in ["medium"]:
            self.log(f"Medium-priority support ticket created for User {user_id}. Assigning to general team.")
            return {"status": "success", "action": "assigned_support", "details": f"Support assigned to user {user_id}"}
        elif request_type == "billing" and priority_level in ["medium"]:
            self.log(f"Medium-priority billing issue detected for User {user_id}. Scheduling review.")
            return {"status": "success", "action": "scheduled_review", "details": f"Billing review scheduled for user {user_id}"}
        elif request_type == "technical" and priority_level in ["medium"]:
            self.log(f"Medium-priority technical issue reported by User {user_id}. Creating standard ticket.")
            return {"status": "success", "action": "standard_ticket", "details": f"Standard ticket created for user {user_id}"}
        elif request_type == "support" and priority_level in ["low"]:
            self.log(f"Low-priority support ticket created for User {user_id}. Queuing for batch processing.")
            return {"status": "success", "action": "queued_support", "details": f"Support queued for user {user_id}"}
        elif request_type == "billing" and priority_level in ["low"]:
            self.log(f"Low-priority billing issue detected for User {user_id}. Adding to monthly digest.")
            return {"status": "success", "action": "monthly_digest", "details": f"Billing added to user {user_id}'s summary"}
        elif request_type == "technical" and priority_level in ["low"]:
            self.log(f"Low-priority technical issue reported by User {user_id}. Logging for future analysis.")
            return {"status": "success", "action": "logged_analysis", "details": f"Issue logged for user {user_id}"}
        else:
            self.log("Error: No matching condition found for this combination")
            return {"status": "error", "message": "No applicable processing rule defined"}
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    test_cases = [
        (101, "support", "high"),
        (205, "billing", "medium"),
        (399, "technical", "low"),
        (-5, "support", "high"),
        (400, "unknown_type", "high"),
    ]
    for user_id, req_type, prio in test_cases:
        result = engine.process_request(user_id, req_type, prio)