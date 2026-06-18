import json
from typing import Any, Dict
def get_handler(payload: Dict[str, Any]) -> callable:
    decision_key = payload.get("decision")
    handlers_map = {
        "approve": approve_request,
        "reject": reject_request,
        "pending": pending_request
    }
    return handlers_map.get(decision_key)
def approve_request(payload: Dict[str, Any]) -> str:
    request_id = payload["request_id"]
    message = f"Request {request_id} has been approved."
    return json.dumps({"status": "success", "message": message})
def reject_request(payload: Dict[str, Any]) -> str:
    request_id = payload["request_id"]
    reason = payload.get("reason", "No specific reason provided")
    message = f"Request {request_id} has been rejected. Reason: {reason}"
    return json.dumps({"status": "failed", "message": message})
def pending_request(payload: Dict[str, Any]) -> str:
    request_id = payload["request_id"]
    message = f"Request {request_id} is still under review."
    return json.dumps({"status": "pending", "message": message})
if __name__ == '__main__':
    sample_payloads = [
        {"decision": "approve", "request_id": 101},
        {"decision": "reject", "request_id": 102, "reason": "Invalid format"},
        {"decision": "pending", "request_id": 103}
    ]
    for payload in sample_payloads:
        handler = get_handler(payload)
        response = handler(payload)
        print(response)