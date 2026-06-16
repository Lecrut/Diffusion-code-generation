import json
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
    def format_response(self, status_code, message=None):
        if not isinstance(status_code, int) or status_code < 100 or status_code > 599:
            return {"error": "Invalid HTTP Status Code", "code": None}
        code_name = self.status_codes.get(status_code, f"Unknown ({status_code})")
        response_data = {
            "success": True if status_code < 400 else False,
            "message": message or "",
            "http_status": status_code,
            "reason_phrase": code_name
        }
        return {"data": response_data}
if __name__ == '__main__':
    handler = ResponseHandler()
    test_cases = [200, 401, 503]
    for status in test_cases:
        result = handler.format_response(status)
        print(json.dumps(result))