class StateMachine:
    def __init__(self):
        self.state = "IDLE"
    def process(self, condition_value):
        if self.state == "IDLE":
            if condition_value > 10:
                print("Action executed in IDLE state")
                self.state = "ACTIVE"
            else:
                print("Condition not met for IDLE state")
        elif self.state == "ACTIVE":
            if condition_value < 5:
                print("Transitioning to PAUSED state")
                self.state = "PAUSED"
            else:
                print("Continuing in ACTIVE state")
        elif self.state == "PAUSED":
            if condition_value > 8:
                print("Resuming from PAUSED state")
                self.state = "ACTIVE"
            else:
                print("Remaining in PAUSED state")
if __name__ == '__main__':
    machine = StateMachine()
    test_values = [12, 3, 4, 9]
    for val in test_values:
        print(f"Processing value: {val}")
        machine.process(val)
        if val == 12 or val == 4:
            break
        print("---")