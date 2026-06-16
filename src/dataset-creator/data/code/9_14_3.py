import json
from typing import Dict, Any
class WorkflowRouter:
    def __init__(self):
        self.routing_rules = [
            {
                "priority": 10,
                "conditions": {"department": "sales"},
                "action": {"target_queue": "high_value_sales", "handler_type": "automated_email"}
            },
            {
                "priority": 20,
                "conditions": {"project_status": "active", "risk_level": "low"},
                "action": {"target_queue": "development_sprint", "handler_type": "auto_commit"}
            },
            {
                "priority": 30,
                "conditions": {"department": "it_support"},
                "action": {"target_queue": "ticket_system", "handler_type": "triage_bot"}
            }
        ]
    def evaluate_rule(self, input_data: Dict[str, Any]) -> bool:
        for rule in self.routing_rules:
            if all(input_data.get(k) == v for k, v in rule["conditions"].items()):
                return True
        return False
    def route_request(self, request_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        matched_rule = None
        for rule in self.routing_rules:
            if self.evaluate_rule(data):
                matched_rule = rule
                break
        result = {
            "request_id": request_id,
            "status": "routed",
            "rule_applied": json.dumps(matched_rule) if matched_rule else None,
            "target_queue": matched_rule["action"]["target_queue"] if matched_rule else "default_general"
        }
        return result
def main():
    router = WorkflowRouter()
    sample_request_data = {
        "request_id": "REQ-20231027-001",
        "department": "sales",
        "project_status": None,
        "risk_level": None
    }
    response = router.route_request(
        request_id=sample_request_data["request_id"],
        data=sample_request_data.copy()
    )
    print(json.dumps(response, indent=2))
if __name__ == '__main__':
    main()