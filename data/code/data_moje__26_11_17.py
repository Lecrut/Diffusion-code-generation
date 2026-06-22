class VotingEligibilityManager:
    def __init__(self, minimum_voting_age=18):
        self.minimum_voting_age = minimum_voting_age
        self.records = {}

    def add_record(self, person_id, age, citizenship_status=True):
        self.records[person_id] = {
            'age': age,
            'citizenship_status': citizenship_status
        }

    def remove_record(self, person_id):
        if person_id in self.records:
            del self.records[person_id]

    def check_eligibility(self, person_id):
        if person_id not in self.records:
            return False

        record = self.records[person_id]
        return (
            record['age'] >= self.minimum_voting_age and
            record['citizenship_status'] is True
        )

    def get_eligible_voters(self):
        eligible = []
        for person_id, record in self.records.items():
            if self.check_eligibility(person_id):
                eligible.append(person_id)
        return eligible

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_record('person1', 25, True)
    manager.add_record('person2', 16, True)
    manager.add_record('person3', 20, False)
    manager.add_record('person4', 18, True)

    print(manager.check_eligibility('person1'))
    print(manager.check_eligibility('person2'))
    print(manager.check_eligibility('person3'))
    print(manager.check_eligibility('person4'))
    print(manager.get_eligible_voters())