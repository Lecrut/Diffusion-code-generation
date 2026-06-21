class VotingEligibilityManager:
    def __init__(self):
        self.voting_age = 18
        self.records = {}

    def check_eligibility(self, name, age, citizenship_status=True, criminal_record=False):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        
        is_eligible = (
            age >= self.voting_age and
            citizenship_status is True and
            criminal_record is False
        )
        
        self.records[name] = {
            "age": age,
            "citizenship_status": citizenship_status,
            "criminal_record": criminal_record,
            "eligible": is_eligible
        }
        
        return is_eligible

    def get_record(self, name):
        return self.records.get(name)

    def update_voting_age(self, new_age):
        if new_age < 0:
            raise ValueError("Voting age must be non-negative")
        self.voting_age = new_age

if __name__ == "__main__":
    manager = VotingEligibilityManager()
    
    print(manager.check_eligibility("Alice", 20, True, False))
    print(manager.check_eligibility("Bob", 16, True, False))
    print(manager.check_eligibility("Charlie", 25, False, False))
    print(manager.check_eligibility("Diana", 30, True, True))
    
    print(manager.get_record("Alice"))
    print(manager.get_record("Bob"))