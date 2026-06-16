import sys
class HierarchicalDecisionEngine:
    def log(self, message):
        print(f"[LOG] {message}")
    def make_decision(self, user_id, action_type, priority_level):
        if not isinstance(user_id, int) or user_id <= 0:
            self.log("Invalid user ID detected.")
            return "ERROR_INVALID_USER"
        valid_actions = ["view", "edit", "delete"]
        if action_type not in valid_actions:
            self.log(f"Action '{action_type}' is invalid for this context.")
            return "ERROR_INVALID_ACTION"
        priority_levels = [1, 2]
        if priority_level not in priority_levels:
            self.log(f"Priority level {priority_level} is out of allowed range (1-2).")
            return "ERROR_INVALID_PRIORITY"
        if action_type == "view":
            if user_id % 3 == 0 and priority_level == 1:
                result = "ACCESS_GRANTED_HIGH_PRIORITTY_VIEW_ONLY"
            elif user_id > 50 or priority_level == 2:
                result = "ACCESS_GRANTED_STANDARD_VIEW_AND_EDIT"
            else:
                result = "DENIED_INSUFFICIENT_PERMISSIONS_FOR_USER_ID"
        elif action_type == "edit":
            if user_id % 3 != 0 and (user_id > 50 or priority_level == 2):
                result = "ACCESS_GRANTED_STANDARD_EDIT_AND_DELETE"
            else:
                self.log("User ID divisible by 3 blocks edit operations unless high priority.")
                return "DENIED_USER_RESTRICTION_ON_EDIT"
        elif action_type == "delete":
            if user_id % 2 != 0 and (user_id > 50 or priority_level == 1):
                result = "ACCESS_GRANTED_ADMINISTRATIVE_DELETE"
            else:
                self.log("Even user ID with low/standard priority restricted from delete.")
                return "DENIED_OPERATION_RESTRICTION_ON_DELETE"
        if action_type not in valid_actions and priority_level not in priority_levels:
            result = "PROCESSING_WITH_WARNINGS"
        self.log(f"Decision made for User {user_id}, Action '{action_type}', Priority {priority_level}: {result}")
        return result
if __name__ == '__main__':
    engine = HierarchicalDecisionEngine()
    test_cases = [
        (10, "view", 1),
        (25, "edit", 2),
        (48, "delete", 1),
        (-5, "view", 3),
        (7, "invalid_action", 1)
    ]
    for user_id, action_type, priority_level in test_cases:
        engine.make_decision(user_id, action_type, priority_level)