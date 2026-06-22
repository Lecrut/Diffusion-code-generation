from typing import Dict, Any

class VoterValidationError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

MIN_AGE: int = 18
CITIZEN_LABEL: str = "citizen"
REQUIRED_KEYS: tuple = ("age", "citizenship", "registered")

def _verify_age(age: Any) -> None:
    if not isinstance(age, int):
        raise VoterValidationError("Age must be an integer")
    if age < 0:
        raise VoterValidationError("Age cannot be negative")

def _verify_citizenship(citizenship: Any) -> bool:
    if isinstance(citizenship, str):
        return citizenship.lower() == CITIZEN_LABEL
    if isinstance(citizenship, bool):
        return citizenship
    raise VoterValidationError("Citizenship must be a string or boolean")

def _verify_registration(registered: Any) -> bool:
    if isinstance(registered, bool):
        return registered
    if isinstance(registered, str):
        return registered.lower() in ("true", "yes", "1")
    raise VoterValidationError("Registration status must be boolean or string")

def check_voter_eligibility(attributes: Dict[str, Any]) -> str:
    missing = set(REQUIRED_KEYS) - set(attributes.keys())
    if missing:
        raise VoterValidationError(f"Missing required attributes: {sorted(missing)}")

    _verify_age(attributes["age"])
    is_citizen = _verify_citizenship(attributes["citizenship"])
    is_registered = _verify_registration(attributes["registered"])

    if attributes["age"] < MIN_AGE:
        return "ineligible: under age"
    if not is_citizen:
        return "ineligible: not a citizen"
    if not is_registered:
        return "ineligible: not registered"
    return "eligible"

if __name__ == "__main__":
    valid_voter: Dict[str, Any] = {
        "age": 30,
        "citizenship": "Citizen",
        "registered": True
    }
    underage_voter: Dict[str, Any] = {
        "age": 16,
        "citizenship": "citizen",
        "registered": True
    }
    unregistered_voter: Dict[str, Any] = {
        "age": 25,
        "citizenship": True,
        "registered": False
    }
    non_citizen_voter: Dict[str, Any] = {
        "age": 40,
        "citizenship": "resident",
        "registered": True
    }

    print(check_voter_eligibility(valid_voter))
    print(check_voter_eligibility(underage_voter))
    print(check_voter_eligibility(unregistered_voter))
    print(check_voter_eligibility(non_citizen_voter))