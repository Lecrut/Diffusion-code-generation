import sys
def validate_input(value: str) -> bool:
    if not value.strip():
        return False
    try:
        float(value.strip())
        return True
    except ValueError:
        return False
class StateManager:
    def __init__(self):
        self.state = "IDLE"
    def process_request(self, input_data) -> str:
        if not isinstance(input_data, str):
            return "ERROR: Input must be a string."
        if validate_input(input_data):
            try:
                num_value = float(input_data.strip())
                if self.state == "IDLE":
                    if 0 <= num_value <= 100:
                        self.state = "ACTIVE"
                        return f"State transitioned to ACTIVE. Value accepted: {num_value}"
                    else:
                        return "ERROR: Value out of range [0, 100] for IDLE state."
                elif self.state == "ACTIVE":
                    if num_value < 50:
                        self.state = "WARNING"
                        return f"State transitioned to WARNING. Threshold crossed at {num_value}."
                    else:
                        return f"State remains ACTIVE. Value within bounds ({num_value})."
                elif self.state == "WARNING":
                    if num_value >= 80:
                        self.state = "CRITICAL"
                        return f"State transitioned to CRITICAL. Critical threshold reached at {num_value}."
                    else:
                        return f"State remains WARNING. Value below critical ({num_value})."
                elif self.state == "CRITICAL":
                    if num_value > 95:
                        return "ERROR: System overload detected. Shutting down gracefully."
                    else:
                        return f"State remains CRITICAL. Attempting recovery with value {num_value}."
            except ValueError:
                return "ERROR: Invalid numeric format in input data."
        else:
            return "ERROR: Input validation failed for state transition logic."
if __name__ == '__main__':
    sample_inputs = [
        "",
        "abc",
        "-50.5",
        "150",
        "75.2",
        "98.9"
    ]
    manager = StateManager()
    for i, data in enumerate(sample_inputs):
        result = manager.process_request(data)
        print(f"Iteration {i}: Input='{data}' -> Output: '{result}'")