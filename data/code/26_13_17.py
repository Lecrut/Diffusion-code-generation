from typing import Any

class VoterEligibilityChecker:
    def __init__(self, min_age: int = 18) -> None:
        self.min_age = min_age

    def check_eligibility(self, attributes: dict[str, Any]) -> bool:
        try:
            age = attributes.get("age")
            citizen = attributes.get("citizen")
            registered = attributes.get("registered")

            if not isinstance(age, int) or age < 0:
                raise ValueError("Age must be a non-negative integer")
            if not isinstance(citizen, bool):
                raise ValueError("Citizen status must be a boolean")
            if not isinstance(registered, bool):
                raise ValueError("Registered status must be a boolean")

            return age >= self.min_age and citizen is True and registered is True
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Invalid voter attributes: {e}") from e

if __name__ == "__main__":
    checker = VoterEligibilityChecker(18)
    voter_a = {"age": 25, "citizen": True, "registered": True}
    voter_b = {"age": 17, "citizen": True, "registered": True}
    voter_c = {"age": 30, "citizen": False, "registered": True}
    print(checker.check_eligibility(voter_a))
    print(checker.check_eligibility(voter_b))
    print(checker.check_eligibility(voter_c))