import json
class WorkflowRouter:
    def __init__(self):
        self.rules = [
            {"condition": lambda x: "urgent" in str(x).lower(), "action": "escalate"},
            {"condition": lambda x: "billing" in str(x).lower() and not "urgent" in str(x).lower(), "action": "finance_team"},
            {"condition": lambda x: len(str(x)) > 50, "action": "review_queue"},
        ]
    def route(self, input_data):
        for rule in self.rules:
            if rule["condition"](input_data):
                return {
                    "status": "routed",
                    "rule_applied": rule["action"],
                    "priority": 10 - len(rule)
                }
        return {"status": "default_queue"}
if __name__ == '__main__':
    test_cases = [
        "URGENT: Server Down Now!",
        "Billing inquiry for invoice #452",
        "This is a very long support ticket description that exceeds fifty characters in length"
    ]
    results = []
    router = WorkflowRouter()
    for case in test_cases:
        result = router.route(case)
        results.append({"input": case, "output": json.dumps(result)})
    print(json.dumps(results))