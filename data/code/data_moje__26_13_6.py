from typing import Dict, Any, Tuple

def check_voter_eligibility(attributes: Dict[str, Any]) -> Tuple[bool, str]:
    try:
        age = attributes.get("age")
        if age is None:
            return False, "Missing age attribute"
        if not isinstance(age, int) or age < 0:
            return False, "Invalid age value"
        
        citizenship = attributes.get("citizenship")
        if citizenship is None:
            return False, "Missing citizenship attribute"
        if not isinstance(citizenship, str) or citizenship.lower() not in ["citizen", "national"]:
            return False, "Non-citizen or invalid citizenship status"
        
        registration = attributes.get("registered")
        if registration is None:
            return False, "Missing registration status"
        if not isinstance(registration, bool):
            return False, "Invalid registration status"
        if not registration:
            return False, "Not registered to vote"
        
        disqualification = attributes.get("disqualified")
        if disqualification is None:
            disqualification = False
        if not isinstance(disqualification, bool):
            return False, "Invalid disqualification status"
        if disqualification:
            return False, "Voter is currently disqualified"
        
        if age < 18:
            return False, "Age requirement not met (must be 18 or older)"
            
        return True, "Eligible to vote"
    
    except Exception:
        return False, "An unexpected error occurred while processing attributes"

if __name__ == "__main__":
    sample_voter = {
        "age": 25,
        "citizenship": "citizen",
        "registered": True,
        "disqualified": False
    }
    result = check_voter_eligibility(sample_voter)
    print(result)