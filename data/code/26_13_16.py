from typing import Any, Dict, Optional, Tuple

def check_voter_eligibility(attributes: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
    age = attributes.get("age")
    citizenship = attributes.get("citizenship")
    registration = attributes.get("registered", False)

    if not isinstance(age, int):
        return False, "Age must be an integer."
    
    if age < 18:
        return False, "Must be at least 18 years old."
    
    if citizenship != "citizen":
        return False, "Must be a citizen to vote."
    
    if not registration:
        return False, "Must be registered to vote."

    return True, None

if __name__ == "__main__":
    sample_voter_1 = {"age": 25, "citizenship": "citizen", "registered": True}
    sample_voter_2 = {"age": 17, "citizenship": "citizen", "registered": True}
    sample_voter_3 = {"age": 30, "citizenship": "resident", "registered": True}
    sample_voter_4 = {"age": 40, "citizenship": "citizen", "registered": False}

    result_1 = check_voter_eligibility(sample_voter_1)
    result_2 = check_voter_eligibility(sample_voter_2)
    result_3 = check_voter_eligibility(sample_voter_3)
    result_4 = check_voter_eligibility(sample_voter_4)

    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)