class VotingEligibilityManager:
    def __init__(self, minimum_voting_age=18):
        self.minimum_voting_age = minimum_voting_age
        self.records = {}

    def add_voter(self, voter_id, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.records[voter_id] = age

    def remove_voter(self, voter_id):
        if voter_id in self.records:
            del self.records[voter_id]

    def is_eligible(self, voter_id):
        if voter_id not in self.records:
            return False
        age = self.records[voter_id]
        return age >= self.minimum_voting_age

    def get_voter_age(self, voter_id):
        if voter_id not in self.records:
            return None
        return self.records[voter_id]

    def list_eligible_voters(self):
        eligible = []
        for voter_id, age in self.records.items():
            if age >= self.minimum_voting_age:
                eligible.append(voter_id)
        return eligible

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_voter(1, 25)
    manager.add_voter(2, 15)
    manager.add_voter(3, 18)
    manager.add_voter(4, 17)
    print(manager.is_eligible(1))
    print(manager.is_eligible(2))
    print(manager.is_eligible(3))
    print(manager.is_eligible(4))
    print(manager.list_eligible_voters())
    print(manager.get_voter_age(1))
    print(manager.get_voter_age(2))