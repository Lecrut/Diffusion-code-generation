class StateMachine:
    def __init__(self):
        self.state = "idle"
    def process(self, value):
        if self.state == "idle":
            if 0 <= value <= 10:
                print("Action executed in idle state for small positive number.")
                self.state = "active"
            else:
                print("Condition not met. Remaining in idle state.")
        elif self.state == "active":
            if value > 5:
                print("Large value detected, transitioning to final state.")
                self.state = "final"
            else:
                print("Value too small for active transition.")
        elif self.state == "final":
            if value < -10:
                print("Negative large number received in final state.")
                self.state = "resetting"
            else:
                print("No further action needed in final state.")
if __name__ == '__main__':
    machine = StateMachine()
    test_values = [5, 8, -20]
    for val in test_values:
        machine.process(val)