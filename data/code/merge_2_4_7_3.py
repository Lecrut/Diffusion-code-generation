import json
from typing import Any, Callable
def get_handler(payload: dict) -> Callable | None:
    decision_key = payload.get("decision")
    handlers_map = {
        "approve": approve_request,
        "reject": reject_request,
        "escalate": escalate_request,
    }
    return handlers_map.get(decision_key.lower())
def approve_request(payload: dict) -> str:
    user_id = payload.get("user")
    amount = float(payload.get("amount", 0))
    return f"Request approved for {user_id}: ${amount:.2f}"
def reject_request(payload: dict) -> str:
    reason = payload.get("reason", "Policy violation")
    user_id = payload.get("user")
    return f"Request rejected for {user_id}. Reason: {reason}"
def escalate_request(payload: dict) -> str:
    priority = payload.get("priority", "medium")
    ticket_number = payload.get("ticket_num", "#000")
    return f"Escalated to manager. Ticket #{ticket_number} (Priority: {priority})"
if __name__ == '__main__':
    sample_payloads = [
        {"decision": "approve", "user": "Alice", "amount": 500},
        {"decision": "reject", "reason": "Insufficient funds"},
        {"decision": "escalate", "priority": "high"}
    ]
    for payload in sample_payloads:
        try:
            handler = get_handler(payload)
            if handler is None:
                print(f"No handler found for decision '{payload['decision']}'")
            else:
                result = handler(payload)
                print(result)
        except Exception as e:
            print(f"Error processing payload {json.dumps(payload)}: {e}")