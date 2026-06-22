class VotingEligibilityManager:
    MIN_AGE = 18

    def __init__(self, citizen_id: str, age: int, registered: bool = False):
        self.citizen_id = citizen_id
        self.age = age
        self.registered = registered

    def is_eligible(self) -> bool:
        if not self.registered:
            return False
        if self.age < self.MIN_AGE:
            return False
        if self.age > 150:
            return False
        return True

    def get_status(self) -> str:
        if self.is_eligible():
            return "Eligible"
        reasons = []
        if not self.registered:
            reasons.append("Not registered")
        if self.age < self.MIN_AGE:
            reasons.append(f"Age {self.age} is below minimum {self.MIN_AGE}")
        if self.age > 150:
            reasons.append("Age exceeds maximum limit")
        if not reasons:
            return "Eligible"
        return f"Not Eligible: {', '.join(reasons)}"

if __name__ == '__main__':
    manager = VotingEligibilityManager("CIT-12345", 25, True)
    print(manager.get_status())
    print(manager.is_eligible())

    underage_manager = VotingEligibilityManager("CIT-67890", 16, True)
    print(underage_manager.get_status())

    unregistered_manager = VotingEligibilityManager("CIT-11111", 20, False)
    print(unregistered_manager.get_status())