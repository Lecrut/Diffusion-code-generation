class StateMachine:
    def __init__(self):
        self.state = "idle"
    def process(self, condition_value):
        if condition_value == 10 and self.state == "idle":
            self.action_start()
            self.state = "running"
        elif condition_value > 20:
            self.action_stop()
            self.state = "stopped"
        else:
            print("Condition not met for current state")
    def action_start(self):
        print("Starting process initiated.")
    def action_stop(self):
        print("Process stopped due to high value detected.")
if __name__ == '__main__':
    machine = StateMachine()
    result_1 = machine.process(10)
    result_2 = machine.process(5)
    result_3 = machine.process(25)
    print(f"Final State after all checks: {machine.state}")