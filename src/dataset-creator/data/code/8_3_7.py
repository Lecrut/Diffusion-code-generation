import json
class ResponseHandler:
    def __init__(self):
        self.status_codes = {}
    def _validate_input(self, data_type, value):
        if isinstance(value, dict) and 'type' in data_type and data_type['type'] == 'string':
            return len(str(value)) > 0
        elif isinstance(value, int) and 'min_value' in data_type:
            return value >= data_type['min_value']
        return True
    def _generate_response(self, status_code, message):
        response = {
            "status": status_code,
            "message": message,
            "timestamp": None                                             
        }
        headers = {}
        if status_code == 200:
            headers["Content-Type"] = "application/json"
        elif status_code in [400, 401]:
            headers["X-Error-Cause"] = message
        return {**response, **headers}
    def handle_request(self, data_type, input_value):
        if not self._validate_input(data_type, input_value):
            response_data = "Invalid Input"
            status_code_map = {400: 1, 500: 2}
            error_status = next(iter(status_code_map.items()), (400, 1))[0]
        else:
            response_data = json.dumps({"success": True})
            return self._generate_response(200, "Success")
if __name__ == '__main__':
    handler = ResponseHandler()
    test_cases = [
        {"data_type": {"type": "string"}, "input_value": ""},
        {"data_type": {"min_value": 18}, "input_value": 50}
    ]
    for case in test_cases:
        result = handler.handle_request(case["data_type"], case["input_value"])
        print(json.dumps(result, indent=4))