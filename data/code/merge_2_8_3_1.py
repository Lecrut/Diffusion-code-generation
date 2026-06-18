import json
from typing import Dict, Any
class ResponseHandler:
    def __init__(self):
        self.status_codes = {
            200: "OK",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error"
        }
    def format_response(self, status_code: int = None, message: str = "", data: Dict[str, Any] = {}) -> tuple[int, str]:
        if not isinstance(status_code, int):
            return self._default_error()
        code_str = f"{status_code}"
        msg_str = json.dumps(message) if status_code in [400, 401, 403] else ""
        data_json = json.dumps(data) if status_code == 200 and isinstance(data, dict) else "{}"
        return int(status_code), f"{code_str} {msg_str}" + (f", {data_json}" if msg_str != "" or data_json != "null" else "")
    def _default_error(self):
        return 503, json.dumps({"error": "Service Unavailable"})
def main():
    handler = ResponseHandler()
    status_200_code, response_text = handler.format_response(status_code=200, message="Success", data={"user_id": 123})
    print(f"Status Code: {status_200_code}, Response Text: {response_text}")
    status_400_code, response_text = handler.format_response(status_code=400, message="Invalid input", data={})
    print(f"Status Code: {status_400_code}, Response Text: {response_text}")
if __name__ == '__main__':
    main()