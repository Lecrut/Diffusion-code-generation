from typing import Any, Dict, List

REQUIRED_KEYS: List[str] = ["age", "citizenship", "is_registered"]
CITIZENSHIP_LABEL: str = "citizen"
MINIMUM_AGE: int = 18

class VoterValidationException(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(self.message)

def _validate_attributes(attributes: Dict[str, Any]) -> None:
    missing_keys: List[str] = [key for key in REQUIRED_KEYS if key not in attributes]
    if missing_keys:
        raise VoterValidationException(f"Missing required attributes: {', '.join(missing_keys)}")
    if not isinstance(attributes["age"], int):
        raise VoterValidationException("Age must be an integer.")
    if attributes["age"] < 0:
        raise VoterValidationException("Age cannot be negative.")
    if not isinstance(attributes["citizenship"], str):
        raise VoterValidationException("Citizenship status must be a string.")
    if not isinstance(attributes["is_registered"], bool):
        raise VoterValidationException("Registration status must be a boolean.")

def determine_eligibility(attributes: Dict[str, Any]) -> str:
    _validate_attributes(attributes)
    age: int = attributes["age"]
    citizenship: str = attributes["citizenship"].lower()
    is_registered: bool = attributes["is_registered"]

    if age < MINIMUM_AGE:
        return "ineligible"
    if citizenship != CITIZENSHIP_LABEL:
        return "ineligible"
    if not is_registered:
        return "ineligible"
    return "eligible"

if __name__ == '__main__':
    sample_voter: Dict[str, Any] = {
        "age": 21,
        "citizenship": "citizen",
        "is_registered": True
    }
    result: str = determine_eligibility(sample_voter)
    print(result)