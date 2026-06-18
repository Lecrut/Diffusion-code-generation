import json
class ResponseHandler:
    def __init__(self):
        self.success_codes = [200, 201]
        self.client_errors = [400, 401, 403, 404]
        self.server_errors = [500, 502, 503]
    def format_response(self, status_code: int, message: str) -> dict:
        if status_code in self.success_codes:
            return {"status": "success", "code": status_code, "message": message}
        elif any(code == status_code for code in self.client_errors):
            return {"status": "client_error", "code": status_code, "message": message}
        elif any(code == status_code for code in self.server_errors):
            return {"status": "server_error", "code": status_code, "message": message}
        else:
            return {"status": "unknown", "code": status_code, "message": f"Unhandled code {status_code}"}
if __name__ == '__main__':
    handler = ResponseHandler()
    test_cases = [
        (201, "Resource created successfully"),
        (403, "Access denied due to insufficient permissions"),
        (500, "Internal server error occurred during processing")
    ]
    for code, msg in test_cases:
        result = handler.format_response(code, msg)
        print(json.dumps(result))