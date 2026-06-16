import json
from typing import Any, Dict
class ResponseHandler:
    def __init__(self):
        self.success_codes = [200, 201]
        self.client_errors = [400, 401, 403, 404]
        self.server_errors = [500, 502, 503]
    def format_response(self, status_code: int, message: str, data: Any) -> Dict[str, Any]:
        if not isinstance(status_code, int):
            raise ValueError("Status code must be an integer")
        response_body = {
            "status": self._get_status_label(status_code),
            "message": message,
            "data": json.dumps(data) if data is not None else ""
        }
        return {
            "code": status_code,
            "body": response_body
        }
    def _get_status_label(self, code: int) -> str:
        for group in [self.success_codes, self.client_errors, self.server_errors]:
            if code in group:
                return f"{group[0]}_{code}"
        return "UNKNOWN"
if __name__ == '__main__':
    handler = ResponseHandler()
    success_data = {"user_id": 123, "action": "created"}
    response_200 = handler.format_response(200, "Request processed successfully", success_data)
    invalid_input_error = {
        "field": "email", 
        "error": "Invalid format"
    }
    response_400 = handler.format_response(400, "Validation failed: Invalid email provided", invalid_input_error)
    simulated_failure_data = {"retry_after": 3600}
    response_500 = handler.format_response(500, "Internal server error occurred during processing", simulated_failure_data)
    print(json.dumps(response_200))
    print(json.dumps(response_400))
    print(json.dumps(response_500))