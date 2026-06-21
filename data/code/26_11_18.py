class VotingEligibilityManager:
    def __init__(self, minimum_age=18):
        self.minimum_age = minimum_age
        self.records = {}

    def add_record(self, name, age, citizenship_status):
        self.records[name] = {
            "age": age,
            "citizenship_status": citizenship_status,
            "eligible": self._check_eligibility(age, citizenship_status)
        }

    def _check_eligibility(self, age, citizenship_status):
        if not citizenship_status:
            return False
        if age < self.minimum_age:
            return False
        return True

    def check_eligibility(self, name):
        if name not in self.records:
            return None
        return self.records[name]["eligible"]

    def update_age(self, name, new_age):
        if name in self.records:
            self.records[name]["age"] = new_age
            self.records[name]["eligible"] = self._check_eligibility(
                new_age,
                self.records[name]["citizenship_status"]
            )

    def get_all_records(self):
        return self.records

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_record("Alice", 20, True)
    manager.add_record("Bob", 16, True)
    manager.add_record("Charlie", 30, False)
    manager.add_record("Diana", 18, True)

    print(manager.check_eligibility("Alice"))
    print(manager.check_eligibility("Bob"))
    print(manager.check_eligibility("Charlie"))
    print(manager.check_eligibility("Diana"))

    manager.update_age("Bob", 19)
    print(manager.check_eligibility("Bob"))

    print(manager.get_all_records())