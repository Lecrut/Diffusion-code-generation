from typing import Dict, Any, Tuple

def check_voter_eligibility(attributes: Dict[str, Any]) -> Tuple[bool, str]:
    try:
        age = attributes.get("age")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        is_us_citizen = attributes.get("is_us_citizen", False)
        if not isinstance(is_us_citizen, bool):
            raise ValueError("is_us_citizen must be a boolean.")
        registration_status = attributes.get("registration_status", "not_registered")
        if not isinstance(registration_status, str):
            raise ValueError("registration_status must be a string.")
        
        if not is_us_citizen:
            return False, "Not a US citizen."
        if age < 18:
            return False, "Under voting age."
        if registration_status != "registered":
            return False, "Not registered to vote."
        
        return True, "Eligible to vote."
    except KeyError as e:
        return False, f"Missing required attribute: {e}"
    except TypeError as e:
        return False, f"Invalid attribute type: {e}"
    except ValueError as e:
        return False, str(e)
    except Exception:
        return False, "An unexpected error occurred."

if __name__ == '__main__':
    sample_voter = {
        "age": 25,
        "is_us_citizen": True,
        "registration_status": "registered",
        "state": "CA"
    }
    eligibility, reason = check_voter_eligibility(sample_voter)
    print(eligibility)
    print(reason)