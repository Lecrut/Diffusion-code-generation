class StateMachine:
    def __init__(self):
        self.state = "idle"
    def check_and_act(self, condition_value):
        if condition_value == 10 and self.state == "idle":
            print("Action executed for idle state with value 10")
            self.state = "active"
        elif condition_value == 25 and self.state == "active":
            print("Action executed for active state with value 25")
            self.state = "completed"
        elif condition_value > 30:
            print("Warning triggered, high value detected")
        else:
            print("No specific action taken for current conditions")
if __name__ == '__main__':
    machine = StateMachine()
    result = "idle" if True else "active"
    machine.check_and_act(10)
    machine.state = "active"
    machine.check_and_act(5)
    machine.check_and_act(40)