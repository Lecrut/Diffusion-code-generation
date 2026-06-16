import json
def get_handler(payload):
    decision = payload.get("decision", "default")
    if decision == "user":
        return user_handler
    elif decision == "admin":
        return admin_handler
    else:
        return default_handler
def user_handler(request_data):
    status_code = 200
    response_body = {"message": f"Hello, {request_data.get('name', 'User')}!"}
    if request_data.get("action") == "login":
        token = generate_token()
        response_body["token"] = token
    return (status_code, json.dumps(response_body))
def admin_handler(request_data):
    status_code = 201
    response_body = {"message": f"Admin action executed for {request_data.get('resource', 'unknown')}"}
    if request_data.get("action") == "delete":
        resource_id = request_data.get("id", "")
        response_body["deleted"] = True
    return (status_code, json.dumps(response_body))
def default_handler(request_data):
    status_code = 404
    response_body = {"message": f"Default handler received: {request_data}"}
    if request_data.get("action") == "test":
        response_body["result"] = "passed"
    return (status_code, json.dumps(response_body))
def generate_token():
    import secrets
    token_length = 32
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    token = ''.join(secrets.choice(alphabet) for _ in range(token_length))
    return f"tok_{token}"
class RequestRouter:
    def __init__(self):
        self.handlers_map = {
            "user": user_handler,
            "admin": admin_handler,
            "default": default_handler
        }
    def route(self, payload_json_string):
        try:
            payload = json.loads(payload_json_string)
            handler_func = get_handler(payload)
            request_data = payload.get("data", {})
            status_code, response_body = handler_func(request_data)
            return {
                "status": status_code,
                "body": response_body
            }
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}
if __name__ == '__main__':
    router_instance = RequestRouter()
    sample_payloads = [
        {
            "decision": "user",
            "data": {"name": "Alice", "action": "login"},
            "json_string": json.dumps({
                "decision": "user",
                "data": {"name": "Alice", "action": "login"}
            })
        },
        {
            "decision": "admin",
            "data": {"resource": "database", "id": 123, "action": "delete"},
            "json_string": json.dumps({
                "decision": "admin",
                "data": {"resource": "database", "id": 123, "action": "delete"}
            })
        },
        {
            "decision": "unknown",
            "data": {"action": "test"},
            "json_string": json.dumps({
                "decision": "unknown",
                "data": {"action": "test"}
            })
        }
    ]
    for sample in sample_payloads:
        result = router_instance.route(sample["json_string"])
        print(f"Decision: {sample['decision']}")
        print(result)