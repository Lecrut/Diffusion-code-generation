class VotingRecord:
    MIN_AGE = 18
    MAX_AGE = 150

    def __init__(self, name: str, age: int, registration_number: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer")
        if not isinstance(registration_number, str) or not registration_number.strip():
            raise ValueError("Registration number cannot be empty")

        self.name = name
        self.age = age
        self.registration_number = registration_number
        self.is_eligible = self._calculate_eligibility()

    def _calculate_eligibility(self) -> bool:
        return self.MIN_AGE <= self.age <= self.MAX_AGE

    def check_eligibility(self, current_age: int = None) -> bool:
        age_to_check = current_age if current_age is not None else self.age
        if not isinstance(age_to_check, int) or age_to_check < 0:
            raise ValueError("Age must be a non-negative integer")
        return self.MIN_AGE <= age_to_check <= self.MAX_AGE

    def update_age(self, new_age: int) -> None:
        if not isinstance(new_age, int) or new_age < 0:
            raise ValueError("Age must be a non-negative integer")
        self.age = new_age
        self.is_eligible = self._calculate_eligibility()

    def get_record(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "registration_number": self.registration_number,
            "is_eligible": self.is_eligible
        }

if __name__ == '__main__':
    record = VotingRecord("Alice Smith", 25, "REG-123456")
    print(record.get_record())
    print(record.check_eligibility())
    record.update_age(17)
    print(record.get_record())
    print(record.check_eligibility())