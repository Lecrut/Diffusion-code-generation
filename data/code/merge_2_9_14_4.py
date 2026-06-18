import json
from typing import Dict, Any
class WorkflowRouter:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: "urgent" in str(x).lower() and "high" in str(x).lower(), "action": "escalate"},
            {"condition": lambda x: len(str(x)) > 50, "action": "split_task"},
            {"condition": lambda x: "@" in str(x), "action": "notify_team"},
        ]
    def route(self, input_data: Any) -> Dict[str, Any]:
        processed = {
            "input_received": True,
            "actions_taken": [],
            "final_status": "processed"
        }
        for rule in self.rules:
            if rule["condition"](str(input_data)):
                action_name = rule["action"]
                processed["actions_taken"].append(action_name)
                if action_name == "escalate":
                    processed["priority_level"] = 10
                    processed["final_status"] = "critical"
        return processed
def main():
    router = WorkflowRouter()
    sample_inputs = [
        "Project deadline is urgent and high priority",
        "This report contains over fifty pages of data analysis",
        "Meeting scheduled with @john_doe for tomorrow at 3pm",
        "Standard quarterly review request"
    ]
    results = []
    for item in sample_inputs:
        result = router.route(item)
        output_record = {
            "input": item,
            "routing_decision": result["final_status"],
            "triggered_actions": result["actions_taken"]
        }
        if "priority_level" in result:
            output_record["priority_score"] = result["priority_level"]
        results.append(output_record)
    print(json.dumps(results, indent=2))
if __name__ == '__main__':
    main()