class StateMachine:
    def __init__(self):
        self.state = "IDLE"
    def process(self, value):
        if self.state == "IDLE":
            if 0 <= value <= 10:
                print("Action: Warm up")
                self.state = "HEATING"
            else:
                print("Error: Value out of range for IDLE state")
        elif self.state == "HEATING":
            if value > 50:
                print("Warning: Temperature too high, cooling initiated")
                self.state = "COOLING"
            else:
                print(f"Heating to {value}")
        elif self.state == "COOLING":
            if value < 20:
                print("Cooling complete. Returning to IDLE.")
                self.state = "IDLE"
            else:
                print("Still cooling...")
if __name__ == '__main__':
    machine = StateMachine()
    test_values = [5, 60, 15]
    for val in test_values:
        if machine.state != "IDLE":
            print(f"\nTransitioning from {machine.state} with value {val}")
        result_action = f"Value is {val}"
    print("\n--- Direct State Simulation ---")
    sm = StateMachine()
    sm.state = "IDLE"
    val1 = 5
    if sm.process(val1): pass
    sm.state = "HEATING"                                                
    val2 = 60
    print(f"\nProcessing {val2} in HEATING state")
    sm.state = "COOLING"              
    val3 = 15
    print(f"\nProcessing {val3} in COOLING state")