import json
def handle_request(payload):
    decision = payload.get("decision", "default")
    if decision == "login":
        return {"status": "logged_in", "user_id": 1024}
    elif decision == "purchase":
        return {"status": "transaction_failed", "reason": "insufficient_funds"}
    else:
        return {"status": "unknown_action", "message": "decision key not recognized"}
if __name__ == '__main__':
    sample_payload = {
        "request_id": "req_98765",
        "decision": "purchase"
    }
    response = handle_request(sample_payload)
    print(json.dumps(response, indent=2))