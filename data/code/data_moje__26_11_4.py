class VotingEligibilityManager:
    def __init__(self, min_age=18):
        self.min_age = min_age

    def check_eligibility(self, age, is_citizen, is_registered):
        if not isinstance(age, int) or age < 0:
            return False
        if age < self.min_age:
            return False
        if not is_citizen:
            return False
        if not is_registered:
            return False
        return True

    def get_required_age(self):
        return self.min_age

if __name__ == '__main__':
    manager = VotingEligibilityManager(min_age=18)
    print(manager.check_eligibility(20, True, True))
    print(manager.check_eligibility(16, True, True))
    print(manager.check_eligibility(25, False, True))
    print(manager.get_required_age())