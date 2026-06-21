def check_voter_eligibility(voter: dict) -> str:
    if not isinstance(voter, dict):
        raise TypeError("Input must be a dictionary")

    required_keys = ["age", "citizenship", "registered"]
    for key in required_keys:
        if key not in voter:
            raise KeyError(f"Missing required key: {key}")

    try:
        age = int(voter["age"])
    except (ValueError, TypeError):
        raise ValueError("Age must be a valid integer")

    citizenship = voter["citizenship"]
    registered = voter["registered"]

    if not isinstance(citizenship, str):
        raise TypeError("Citizenship must be a string")
    if not isinstance(registered, bool):
        raise TypeError("Registered must be a boolean")

    if age < 18:
        return "Not eligible: under 18"
    if citizenship.lower() != "citizen":
        return "Not eligible: not a citizen"
    if not registered:
        return "Not eligible: not registered"
    return "Eligible"

if __name__ == '__main__':
    voter_1 = {"age": 25, "citizenship": "Citizen", "registered": True}
    voter_2 = {"age": 16, "citizenship": "Citizen", "registered": True}
    voter_3 = {"age": 30, "citizenship": "Permanent Resident", "registered": True}
    voter_4 = {"age": 22, "citizenship": "Citizen", "registered": False}

    print(check_voter_eligibility(voter_1))
    print(check_voter_eligibility(voter_2))
    print(check_voter_eligibility(voter_3))
    print(check_voter_eligibility(voter_4))