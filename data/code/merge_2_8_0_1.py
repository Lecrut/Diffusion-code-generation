class StateMachine:
    def __init__(self):
        self.state = "idle"
    def process(self, value):
        if self.state == "idle":
            if 0 <= value <= 10:
                print("Action executed for idle state.")
                self.state = "active"
            else:
                print("Condition not met in idle state.")
        elif self.state == "active":
            if value > 50:
                print("High threshold detected, switching to high mode.")
                self.state = "high_mode"
            else:
                print("Normal operation continued.")
        elif self.state == "high_mode":
            if value < 30:
                print("Value dropped below safe limit, returning to active.")
                self.state = "active"
            else:
                print("Maintaining high mode conditions.")
if __name__ == '__main__':
    machine = StateMachine()
    test_values = [5, 80, 25]
    for val in test_values:
        result = f"Processing value {val}..."
        print(result)
        machine.process(val)