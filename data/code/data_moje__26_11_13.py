class VotingEligibilityManager:
    def __init__(self):
        self.records = {}
        self.min_voting_age = 18

    def add_record(self, name, age):
        if not isinstance(name, str) or not isinstance(age, int):
            raise ValueError("Name must be a string and age must be an integer.")
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.records[name] = {
            'age': age,
            'eligible': age >= self.min_voting_age
        }

    def is_eligible(self, name):
        if name not in self.records:
            return False
        return self.records[name]['eligible']

    def update_age(self, name, new_age):
        if name not in self.records:
            raise KeyError(f"Name {name} not found in records.")
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.records[name]['age'] = new_age
        self.records[name]['eligible'] = new_age >= self.min_voting_age

    def get_eligible_voters(self):
        eligible = []
        for name, record in self.records.items():
            if record['eligible']:
                eligible.append(name)
        return eligible

    def get_all_records(self):
        return dict(self.records)

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_record("Alice", 20)
    manager.add_record("Bob", 15)
    manager.add_record("Charlie", 18)

    print(manager.is_eligible("Alice"))
    print(manager.is_eligible("Bob"))
    print(manager.is_eligible("Charlie"))
    print(manager.get_eligible_voters())

    manager.update_age("Bob", 21)
    print(manager.is_eligible("Bob"))
    print(manager.get_eligible_voters())