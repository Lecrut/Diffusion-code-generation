import json
from typing import Dict, Any
class WorkflowRouter:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: "urgent" in str(x).lower(), "action": "priority_queue"},
            {"condition": lambda x: "finance" in str(x).lower() and "report" not in str(x).lower(), "action": "audit_system"},
            {"condition": lambda x: len(str(x)) > 50, "action": "long_text_handler"},
        ]
    def route(self, input_data: Any) -> Dict[str, Any]:
        processed = {
            "input_received": True,
            "routing_decision": None,
            "error_message": None,
        }
        for rule in self.rules:
            if rule["condition"](str(input_data)):
                processed["routing_decision"] = rule["action"]
                break
        return processed
def main():
    router = WorkflowRouter()
    sample_input = "Urgent financial report regarding Q3 projections"
    result = router.route(sample_input)
    output_json = json.dumps(result, indent=2)
    print(output_json)
if __name__ == '__main__':
    main()