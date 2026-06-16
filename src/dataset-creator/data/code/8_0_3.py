class StateMachine:
    def __init__(self):
        self.state = "idle"
    def process(self, value):
        if self.state == "idle":
            if 0 <= value <= 10:
                print("Action executed for idle state.")
                self.state = "active"
            elif value < 0 or value > 10:
                print("Invalid input for idle state.")
        elif self.state == "active":
            if value % 2 == 0:
                print("Even number detected in active state.")
                self.state = "completed"
            else:
                print("Odd number ignored in active state.")
        elif self.state == "completed":
            print("Process finished successfully.")
if __name__ == '__main__':
    machine = StateMachine()
    machine.process(5)
    machine.process(-2)
    machine.process(10)
    machine.process(3)