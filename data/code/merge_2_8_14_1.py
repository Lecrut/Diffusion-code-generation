import sys
class HierarchicalDecisionEngine:
    def log(self, message):
        print(f"[LOG] {message}")
    def process_request(self, user_id, request_type, priority_level, budget_available):
        self.log(f"Processing for User ID: {user_id}, Type: {request_type}, Priority: {priority_level}, Budget: {budget_available}")
        if not isinstance(user_id, int) or user_id <= 0:
            return {"status": "error", "message": f"Invalid User ID. Expected positive integer."}
        valid_types = ["purchase", "support", "report"]
        if request_type not in valid_types:
            self.log(f"Warning: Invalid Request Type '{request_type}'. Defaulting to 'purchase'.")
            final_request_type = "purchase"
        else:
            final_request_type = request_type
        priority_levels = [1, 2, 3]
        if priority_level not in priority_levels:
            self.log(f"Warning: Invalid Priority Level '{priority_level}'. Defaulting to 2.")
            final_priority = 2
        else:
            final_priority = priority_level
        budget_thresholds = {100.0, 500.0}
        if not isinstance(budget_available, (int, float)) or budget_available <= 0:
            return {"status": "error", "message": f"Invalid Budget Amount."}
        final_budget = max(0, min(float(budget_available), 10000.0))
        if priority_level == 3 and request_type in ["purchase", "report"]:
            self.log("High Priority Action Detected.")
            decision_logic = {
                "high_priority_purchase": (final_request_type == "purchase" and final_budget >= 500),
                "critical_report": (final_request_type == "report"),
                "standard_action": True,
            }
        elif priority_level in [1, 2]:
            decision_logic = {
                "low_priority_purchase": (final_request_type == "purchase" and final_budget >= 100),
                "medium_support_check": (request_type == "support"),
                "standard_action": True,
            }
        else:
            return {"status": "error", "message": f"No decision logic defined for Priority Level {priority_level}."}
        if final_request_type in ["purchase", "report"]:
            self.log(f"Executing action '{final_request_type}' with budget check.")
            if priority_level == 3 and request_type in ["purchase", "report"] and (decision_logic["high_priority_purchase"] or decision_logic["critical_report"]):
                return {"status": "approved", "action": f"{priority_level}-Level {request_type} Execution"}
        elif final_request_type == "support" and priority_level <= 2:
            self.log(f"Executing support check for user.")
            if budget_available >= 100.0:
                return {"status": "approved", "action": f"{priority_level}-Level Support Resolution"}
            else:
                return {"status": "pending_review", "message": "Insufficient Budget Allocation."}
        self.log("Default fallback action triggered.")
        if final_budget >= 10.0 and priority_level <= 2:
            return {"status": "approved", "action": f"Standard {final_request_type.lower()} Processing"}
        else:
            return {"status": "denied", "message": "Conditions not met for standard processing."}
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    user_id_val = 1042
    request_type_val = "purchase"
    priority_level_val = 3
    budget_available_val = 750.50
    result = engine.process_request(user_id_val, request_type_val, priority_level_val, budget_available_val)
    print(f"\nFinal Result: {result}")