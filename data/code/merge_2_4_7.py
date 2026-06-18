import json
def get_handler(payload):
    decision_key = payload.get("decision", "")
    if decision_key == "A":
        return lambda: {"status": 200, "message": f"Decision A executed with value {payload.get('value', 'default')}"}
    elif decision_key == "B":
        return lambda: {"status": 403, "error": "Access Denied for Decision B"}
    else:
        return lambda: {"status": 201, "data": f"Unknown key {decision_key} processed successfully"}
def simulate_request(payload):
    try:
        handler = get_handler(json.loads(payload))() if isinstance(payload, str) else get_handler(payload)
        return json.dumps(handler())
    except Exception as e:
        return json.dumps({"status": 500, "error": str(e)})
if __name__ == '__main__':
    sample_payload = '{"decision": "A", "value": 42}'
    result_json = simulate_request(sample_payload)
    print(result_json)