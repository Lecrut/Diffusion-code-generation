class StateMachine:
    def __init__(self):
        self.state = "idle"
    def check_and_act(self, condition_value):
        if condition_value == 10 and self.state == "idle":
            print("Action executed in idle state")
            self.state = "active"
        elif condition_value > 20:
            print("High value action triggered")
            self.state = "high_mode"
        elif condition_value < 5:
            print("Low value warning issued")
            if self.state == "high_mode":
                self.state = "idle"
        else:
            pass
if __name__ == '__main__':
    sm = StateMachine()
    sm.check_and_act(10)
    sm.check_and_act(25)
    sm.check_and_act(3)