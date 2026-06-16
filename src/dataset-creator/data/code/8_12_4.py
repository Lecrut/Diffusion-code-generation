import sys
class StateManager:
    def __init__(self):
        self.state = "IDLE"
        self.errors = []
    def validate_input(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number")
        return True
    def handle_transition(self, current_state, new_value):
        try:
            validated = self.validate_input(new_value)
            if current_state == "IDLE":
                if 0 <= new_value < 10:
                    self.state = "ACTIVE"
                    print(f"Transitioned to ACTIVE with value {new_value}")
                elif -5 <= new_value < 0 or 10 <= new_value < 20:
                    self.state = "WARNING"
                    self.errors.append("Value outside standard range")
            elif current_state == "ACTIVE":
                if new_value > 19:
                    self.state = "CRITICAL"
                    print(f"Transitioned to CRITICAL with value {new_value}")
                else:
                    print(f"Maintaining ACTIVE state, value is {new_value}")
            elif current_state == "WARNING":
                if -5 <= new_value < 0:
                    self.state = "CRITICAL"
                    print("Escalated to CRITICAL due to negative threshold")
                else:
                    self.errors.append("Warning condition cleared but state not reset")
        except ValueError as e:
            return f"Validation Error: {e}"
        except Exception as e:
            return f"Unexpected System Failure: {e}"
    def degrade(self):
        if len(self.errors) > 2:
            self.state = "DEGRADED"
            print("System entering DEGRADED mode due to accumulated errors")
            return True
        return False
if __name__ == '__main__':
    manager = StateManager()
    test_cases = [
        ("IDLE", 5),
        ("IDLE", -3.5),
        ("ACTIVE", 10),
        ("ACTIVE", 25),
        ("WARNING", -4),
        ("CRITICAL", 9)
    ]
    for state, value in test_cases:
        result = manager.handle_transition(state, value)
        if not isinstance(result, str):                                            
            print(f"Current State after operation: {manager.state}")
            is_degraded = manager.degrade()
            if is_degraded and manager.state != "DEGRADED":
                print("Error: Degradation check failed")
    final_status = f"Final System State: {manager.state}"