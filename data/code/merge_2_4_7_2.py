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
    message = f"Request approved for {user_id}."
    status_code = 200
    headers = {"Content-Type": "application/json"}
    return (status_code, None, json.dumps({"message": message}))
def handle_reject(payload):
    user_id = payload.get("user", "unknown")
    reason = payload.get("reason", "No specific reason provided.")
    message = f"Request rejected for {user_id}. Reason: {reason}."
    status_code = 403
    headers = {"Content-Type": "application/json"}
    return (status_code, None, json.dumps({"message": message}))
def handle_pending(payload):
    user_id = payload.get("user", "unknown")
    message = f"Request pending for {user_id}."
    status_code = 202
    headers = {"Content-Type": "application/json"}
    return (status_code, None, json.dumps({"message": message}))
def handle_default(payload):
    user_id = payload.get("user", "unknown")
    decision_key = payload.get("decision", "default")
    message = f"Unhandled request for {user_id} with key: {decision_key}"
    status_code = 400
    headers = {"Content-Type": "application/json"}
    return (status_code, None, json.dumps({"message": message}))
def main():
    sample_payload = {
        "decision": "approve",
        "user": "12345"
    }
    handler_func = get_handler(sample_payload)
    status_code, _, response_body = handler_func(sample_payload)
    print(f"Status Code: {status_code}")
    print(response_body)
if __name__ == '__main__':
    main()