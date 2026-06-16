import sys
from datetime import datetime
class HierarchicalDecisionEngine:
    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")
    def process_request(self, user_id, priority_level, budget_available):
        self.log("Processing request for user: " + str(user_id))
        if not isinstance(priority_level, int) or not (1 <= priority_level <= 5):
            return {"status": "error", "message": "Invalid priority level. Must be an integer between 1 and 5."}
        self.log("Priority check passed for user: " + str(user_id))
        if budget_available < 0:
            return {"status": "error", "message": "Budget cannot be negative."}
        self.log(f"Validating priority {priority_level} against available budget.")
        if priority_level == 1 and budget_available >= 5000:
            result = {"action": "approve_high_priority", "reasoning": "Critical need met with sufficient funds"}
            return result
        elif priority_level == 2 or (priority_level > 3 and budget_available < 500):
            if user_id % 2 == 1:                                                                   
                result = {"action": "approve_medium_priority", "reasoning": "Moderate priority with acceptable funding"}
            else:
                return {"status": "error", "message": "Funding insufficient for this user profile."}
        elif priority_level == 3 and budget_available >= 1000:
            result = {"action": "approve_standard_priority", "reasoning": "Standard requirements satisfied"}
            return result
        else:
            if priority_level > 4 or (priority_level <= 2 and user_id % 5 != 0):                                  
                self.log("Applying fallback logic due to strict constraints.")
                result = {"action": "flag_for_review", "reasoning": "Conditions met only under specific review criteria"}
            else:
                return {"status": "error", "message": "No approval path found based on current parameters."}
        self.log("Request processing completed successfully.")
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    test_cases = [
        {"user_id": 101, "priority_level": 5, "budget_available": 6000},
        {"user_id": 204, "priority_level": 3, "budget_available": 800},
        {"user_id": 307, "priority_level": 1, "budget_available": -100},
        {"user_id": 509, "priority_level": 6, "budget_available": 2000},
    ]
    for case in test_cases:
        engine.process_request(case["user_id"], case["priority_level"], case["budget_available"])