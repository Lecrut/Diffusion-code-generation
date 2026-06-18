import json
from typing import Dict, Any
class WorkflowRouter:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: "urgent" in str(x).lower(), "action": "escalate"},
            {"condition": lambda x: "billing" in str(x).lower() and not "urgent" in str(x).lower(), "action": "finance_queue"},
            {"condition": lambda x: len(str(x)) > 50, "action": "complex_review"},
            {"default_action": "standard_processing"}
        ]
    def route(self, input_data: Any) -> Dict[str, Any]:
        normalized_input = str(input_data).lower() if isinstance(input_data, (str, int, float)) else json.dumps(input_data).lower()
        for rule in self.rules[:-1]:
            condition_met = False
            try:
                result = rule["condition"](normalized_input)
                if callable(result):
                    condition_met = bool(result())
                elif isinstance(result, str):
                    condition_met = normalized_input == result.lower()
            except Exception:
                continue
            if condition_met:
                return {
                    "status": "routed",
                    "rule_applied": rule["action"],
                    "input_received": input_data,
                    "priority": self._get_priority(rule["action"])
                }
        default_action = self.rules[-1]["default_action"]
        return {
            "status": "processed",
            "rule_applied": default_action,
            "input_received": input_data,
            "priority": 3
        }
    def _get_priority(self, action: str) -> int:
        priorities = {"escalate": 1, "finance_queue": 2, "complex_review": 4}
        return priorities.get(action, 5)
def main():
    router = WorkflowRouter()
    sample_inputs = [
        "URGENT SERVER FAILURE",
        "Monthly invoice query",
        "This is a very long description of the issue that requires detailed analysis and multiple steps to resolve properly.",
        "12345"
    ]
    results = []
    for input_val in sample_inputs:
        result = router.route(input_val)
        results.append({
            "input": input_val,
            **result
        })
    output_log = {
        "workflow_id": "WF-20231027-A",
        "timestamp": "2023-10-27T14:35:00Z",
        "routing_decisions": results,
        "summary": f"Processed {len(results)} requests successfully."
    }
    print(json.dumps(output_log, indent=2))
if __name__ == '__main__':
    main()