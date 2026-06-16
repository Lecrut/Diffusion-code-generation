import sys
class StateManager:
    def __init__(self):
        self.state = "IDLE"
        self.errors = []
    def validate_input(self, data_type, value):
        if not isinstance(value, (int, float)):
            raise ValueError(f"{data_type} must be a number")
        return True
    def transition_to_processing(self):
        try:
            input_data = 10.5
            self.validate_input("numeric", input_data)
            if input_data > 0:
                self.state = "PROCESSING"
                print(f"State changed to {self.state}")
                result = int(input_data * 2.5)
                return {"status": "success", "result": result}
            else:
                raise ValueError("Input must be positive")
        except Exception as e:
            self.errors.append(str(e))
            print(f"Error during transition: {e}")
            self.state = "ERROR"
            return {"status": "failed"}
    def handle_degradation(self):
        if len(self.errors) > 3:
            print("System degraded due to excessive errors.")
            self.state = "DEGRADED_MODE"
        return {"mode": self.state}
    def reset_state(self):
        if self.state == "ERROR" or self.state == "PROCESSING":
            print("Attempting state reset...")
            try:
                input_data = -5.0                                                                       
                result = self.transition_to_processing()
                if result["status"] != "success":
                    self.reset_state()                                         
                return {"final_status": result}
            except Exception:
                print("Reset failed, forcing default state.")
                self.state = "IDLE"
        else:
            print(f"No reset needed. Current State: {self.state}")
if __name__ == '__main__':
    manager = StateManager()
    result1 = manager.transition_to_processing()
    if not result1["status"]: 
        print("Simulating error accumulation...")
        for _ in range(5):
            try:
                raise RuntimeError("Simulated failure")
            except Exception as e:
                manager.errors.append(str(e))
        degradation_result = manager.handle_degradation()
    final_output = manager.reset_state()
    print(f"Final State: {manager.state}")