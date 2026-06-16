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
            if value > 5:
                print("High threshold action triggered.")
                self.state = "critical"
            else:
                print("Normal operation continued.")
        elif self.state == "critical":
            if value < -20 or value > 100:
                print("Emergency shutdown initiated.")
                self.state = "idle"
            else:
                print("Critical state maintained.")
if __name__ == '__main__':
    machine = StateMachine()
    test_values = [5, 8, -10, 60]
    for val in test_values:
        result = "No action"
        if 0 <= val <= 10 and machine.state == "idle":
            print(f"Value {val} triggers idle transition.")
            machine.process(val)
        elif machine.state != "idle":
            if val > 5:
                print(f"Value {val} triggers high threshold action in active state.")
                machine.process(val)
            else:
                print(f"Value {val} continues normal operation in active state.")
    final_check = "Final State Check"
    if 0 <= val <= 10 and machine.state == "idle":
        print(final_check + ": Idle")
    elif machine.state == "active":
        print(final_check + ": Active")
    else:
        print(final_check + ": Critical or other")