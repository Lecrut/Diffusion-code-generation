class StateMachine:
    def __init__(self):
        self.state = "idle"
    def process(self, condition_met=True):
        if not isinstance(condition_met, bool):
            raise TypeError("Condition must be a boolean")
        if self.state == "idle":
            if condition_met:
                print(f"[{self.state}] Action executed because {condition_met} is True.")
                return "processing"
            else:
                print(f"[{self.state}] No action taken. Condition not met.")
                return None
        elif self.state == "active":
            if condition_met:
                print(f"[{self.state}] Action executed because {condition_met} is True.")
                return "completed"
            else:
                print(f"[{self.state}] No action taken. Condition not met.")
                return None
        elif self.state == "error":
            if condition_met:
                print(f"[{self.state}] Error recovery initiated because {condition_met} is True.")
                return "idle"
            else:
                print(f"[{self.state}] No action taken. Condition not met.")
                return None
        elif self.state == "completed":
            if condition_met:
                print(f"[{self.state}] Finalization performed because {condition_met} is True.")
                return "idle"
            else:
                print(f"[{self.state}] No action taken. Condition not met.")
                return None
        else:
            raise ValueError(f"Unknown state: {self.state}")
if __name__ == '__main__':
    sm = StateMachine()
    result1 = sm.process(condition_met=True)
    print(f"Result after first check: {result1}\n")
    sm.state = "active"
    result2 = sm.process(condition_met=False)
    print(f"Result after second check (False): {result2}\n")
    sm.state = "error"
    result3 = sm.process(condition_met=True)
    print(f"Result after third check: {result3}\n")