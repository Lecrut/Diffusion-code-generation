import json
class WorkflowRouter:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: x.get("priority", 0) >= "high", "action": "escalate"},
            {"condition": lambda x: x.get("department") == "finance" and not x.get("is_urgent"), "action": "audit_queue"},
            {"condition": lambda x: x.get("type") in ["billing", "tax"], "action": "generate_invoice"},
        ]
    def route(self, input_data):
        for rule in self.rules:
            if rule["condition"](input_data):
                return {**input_data, **{"status": rule["action"]}}
        raise ValueError("No matching workflow found")
def main():
    sample_input = {"priority": "high", "department": "sales", "type": "support_ticket"}
    router = WorkflowRouter()
    result = router.route(sample_input)
    print(json.dumps(result, indent=2))
if __name__ == '__main__':
    main()