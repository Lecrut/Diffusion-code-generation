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
        self.log("Priority check passed: " + str(priority_level))
        if budget_available < 0:
            return {"status": "error", "message": "Budget cannot be negative."}
        self.log(f"Budget validation passed. Available funds: {budget_available}")
        if priority_level == 1 and user_id in [1, 2]:
            result = {"action": "grant_full_access", "reasoning": "High priority VIP users receive full access regardless of budget constraints."}
            self.log("Decision made: Grant full access due to high priority VIP status.")
        elif priority_level == 5 and user_id in [3, 4]:
            result = {"action": "grant_full_access", "reasoning": "High priority users with sufficient funds receive full access."}
            if budget_available >= 100:
                self.log("Decision made: Grant full access due to high priority + adequate funding.")
            else:
                return {"status": "error", "message": "Insufficient funds for premium tier despite high priority."}
        elif priority_level == 3 and user_id in [5, 6]:
            result = {"action": "grant_partial_access", "reasoning": "Medium priority users receive partial access based on budget."}
            if budget_available >= 50:
                self.log("Decision made: Grant partial access due to medium priority + adequate funding.")
            else:
                return {"status": "error", "message": "Insufficient funds for standard tier despite medium priority."}
        elif priority_level == 2 and user_id in [7, 8]:
            result = {"action": "grant_partial_access", "reasoning": "Low-medium priority users receive partial access based on budget."}
            if budget_available >= 50:
                self.log("Decision made: Grant partial access due to low-medium priority + adequate funding.")
            else:
                return {"status": "error", "message": "Insufficient funds for standard tier despite low-medium priority."}
        elif priority_level == 4 and user_id in [9, 10]:
            result = {"action": "grant_partial_access", "reasoning": "High-potential users receive partial access based on budget."}
            if budget_available >= 50:
                self.log("Decision made: Grant partial access due to high potential + adequate funding.")
            else:
                return {"status": "error", "message": "Insufficient funds for standard tier despite high potential."}
        elif priority_level == 1 and user_id in [9, 10]:
            result = {"action": "grant_full_access", "reasoning": "High priority users with unique ID receive full access regardless of budget constraints."}
            self.log("Decision made: Grant full access due to high priority + unique status.")
        else:
            return {"status": "error", "message": "No matching criteria found for the provided parameters."}
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    test_cases = [
        (1, 3, 50),
        (2, 4, -10),
        (3, 5, 80),
        (4, 2, 60),
        (5, 3, 20),
        (9, 1, 0)
    ]
    for user_id, priority_level, budget_available in test_cases:
        engine.process_request(user_id, priority_level, budget_available)