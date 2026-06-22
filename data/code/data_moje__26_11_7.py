class VotingEligibilityManager:
    MIN_AGE = 18
    MAX_AGE = 150

    def __init__(self):
        self.records = {}

    def add_record(self, voter_id, age, nationality):
        if not isinstance(voter_id, str) or not voter_id:
            raise ValueError("Voter ID must be a non-empty string.")
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if not isinstance(nationality, str) or not nationality:
            raise ValueError("Nationality must be a non-empty string.")
        
        if age < self.MIN_AGE or age > self.MAX_AGE:
            return False
            
        if age >= self.MIN_AGE and nationality.lower() == "citizen":
            self.records[voter_id] = {"age": age, "eligible": True}
            return True
        else:
            self.records[voter_id] = {"age": age, "eligible": False}
            return False

    def is_eligible(self, voter_id):
        if voter_id not in self.records:
            return False
        return self.records[voter_id]["eligible"]

    def get_status(self, voter_id):
        if voter_id not in self.records:
            return "Unknown"
        record = self.records[voter_id]
        if record["eligible"]:
            return f"Eligible (Age: {record['age']})"
        return f"Ineligible (Age: {record['age']})"

if __name__ == '__main__':
    manager = VotingEligibilityManager()
    manager.add_record("V001", 20, "Citizen")
    manager.add_record("V002", 16, "Citizen")
    manager.add_record("V003", 25, "Non-Citizen")
    
    print(manager.get_status("V001"))
    print(manager.is_eligible("V001"))
    print(manager.get_status("V002"))
    print(manager.is_eligible("V002"))
    print(manager.get_status("V003"))
    print(manager.is_eligible("V003"))