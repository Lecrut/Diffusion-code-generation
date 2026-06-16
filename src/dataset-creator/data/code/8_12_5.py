import sys
def validate_input(value):
    if isinstance(value, (int, float)):
        return True
    elif value is None:
        raise ValueError("Input cannot be null.")
    else:
        raise TypeError(f"Invalid input type: {type(value).__name__}. Expected int or float.")
class StateManager:
    def __init__(self):
        self.state = "INITIALIZED"
        self.error_count = 0
    def process_transition(self, value):
        try:
            validate_input(value)
            if self.state == "INITIALIZED":
                new_state = "PROCESSING"
                print(f"[{new_state}] Transition successful.")
            elif self.state == "PROCESSING":
                result = calculate_output(value)
                if result is not None:
                    new_state = "COMPLETED"
                    print(f"[{new_state}] Output generated successfully.")
                else:
                    raise RuntimeError("Calculation failed unexpectedly.")
            elif self.state == "COMPLETED":
                return GracefulDegradation()
        except (ValueError, TypeError) as e:
            self.error_count += 1
            print(f"[ERROR] Validation failed: {e}")
            if self.error_count >= 3:
                new_state = "FAILED"
                sys.exit(1)
            elif self.state == "PROCESSING":
                new_state = "DEGRADED_PROCESSING"
                print("[WARN] Entering degraded mode.")
        except RuntimeError as e:
            if self.error_count >= 3:
                new_state = "FAILED"
                sys.exit(1)
            elif self.state == "PROCESSING":
                new_state = "DEGRADED_PROCESSING"
                print("[WARN] Entering degraded mode.")
        finally:
            self.state = new_state
        return None
def calculate_output(value):
    try:
        if value < 0:
            raise ValueError("Negative values are not supported in this context.")
        result = abs(int(value) * 2.5)
        return result
    except Exception as e:
        print(f"[CALC] Calculation error: {e}")
        return None
class GracefulDegradation:
    def __init__(self):
        self.status = "DEGRADED"
    def get_status(self):
        return f"System is operating in {self.status} mode."
if __name__ == '__main__':
    manager = StateManager()
    test_cases = [10, -5.5, None, 20]
    for item in test_cases:
        try:
            result = manager.process_transition(item)
            if isinstance(result, GracefulDegradation):
                print(f"Final Status: {result.get_status()}")
        except Exception as e:
            print(f"[CRITICAL] Unhandled exception during transition for value {item}: {e}")