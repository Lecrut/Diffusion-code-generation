import json
class ResponseHandler:
    def __init__(self):
        self.status_map = {
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error"
        }
    def handle_request(self, status_code, constraints_met=True):
        if not isinstance(status_code, int) or status_code < 100 or status_code > 599:
            return {"error": "Invalid status code", "code": None}
        message = self.status_map.get(status_code, f"Unknown Status {status_code}")
        response_data = {
            "success": constraints_met,
            "message": message if not constraints_met else "",
            "data": {} if not constraints_met else {"id": 12345}
        }
        return json.dumps(response_data)
if __name__ == '__main__':
    handler = ResponseHandler()
    result_1 = handler.handle_request(200, True)
    result_2 = handler.handle_request(999, False)
    result_3 = handler.handle_request(400, False)
    print(result_1)
    print(result_2)
    print(result_3)