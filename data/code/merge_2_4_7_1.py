import json
def get_handler(payload):
    decision_key = payload.get("decision", "default")
    handlers = {
        "approve": handle_approve,
        "reject": handle_reject,
        "pending": handle_pending,
        "default": handle_default
    }
    return handlers.get(decision_key, handlers["default"])
def handle_approve(payload):
    user_id = payload.get("user", "unknown")
    status = f"Request approved for {user_id}"
    print(status)
    return {"status": "success", "message": status}
def handle_reject(payload):
    reason = payload.get("reason", "No specific reason provided")
    user_id = payload.get("user", "unknown")
    message = f"Request rejected for {user_id}. Reason: {reason}"
    print(message)
    return {"status": "failed", "message": message}
def handle_pending(payload):
    request_id = payload.get("request_id", "N/A")
    status = f"Request #{request_id} is pending review."
    print(status)
    return {"status": "pending", "message": status}
def handle_default(payload):
    message = "Default handler executed. Check decision key in JSON payload."
    print(message)
    return {"status": "default", "message": message}
if __name__ == '__main__':
    sample_payloads = [
        {
            "decision": "approve",
            "user": "Alice"
        },
        {
            "decision": "reject",
            "reason": "Invalid data format",
            "user": "Bob"
        },
        {
            "decision": "pending",
            "request_id": 1024
        }
    ]
    for payload in sample_payloads:
        try:
            handler = get_handler(payload)
            result = handler(payload)
            print(json.dumps(result, indent=2))
        except Exception as e:
            error_result = {"status": "error", "message": str(e)}
            print(json.dumps(error_result, indent=2))