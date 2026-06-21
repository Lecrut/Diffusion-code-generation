def check_voter_eligibility(voter: dict) -> dict:
    required_keys = {"age", "citizenship", "registered"}
    if not required_keys.issubset(voter.keys()):
        raise ValueError("Missing required voter attributes")
    age = voter["age"]
    citizenship = voter["citizenship"]
    registered = voter["registered"]
    if not isinstance(age, int) or age < 0:
        raise TypeError("Age must be a non-negative integer")
    if not isinstance(citizenship, bool):
        raise TypeError("Citizenship must be a boolean")
    if not isinstance(registered, bool):
        raise TypeError("Registered must be a boolean")
    eligible = age >= 18 and citizenship and registered
    return {"eligible": eligible, "reason": None if eligible else get_ineligibility_reason(age, citizenship, registered)}

def get_ineligibility_reason(age: int, citizenship: bool, registered: bool) -> str:
    if age < 18:
        return "Too young"
    if not citizenship:
        return "Not a citizen"
    if not registered:
        return "Not registered"
    return "Unknown reason"

if __name__ == '__main__':
    voter = {"age": 25, "citizenship": True, "registered": True}
    result = check_voter_eligibility(voter)
    print(result)
    voter2 = {"age": 16, "citizenship": True, "registered": True}
    result2 = check_voter_eligibility(voter2)
    print(result2)
    voter3 = {"age": 30, "citizenship": False, "registered": True}
    result3 = check_voter_eligibility(voter3)
    print(result3)
    voter4 = {"age": 20, "citizenship": True, "registered": False}
    result4 = check_voter_eligibility(voter4)
    print(result4)