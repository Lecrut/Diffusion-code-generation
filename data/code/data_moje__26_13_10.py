def check_voter_eligibility(voter: dict) -> str:
    try:
        age = voter["age"]
        citizenship = voter["citizenship"]
        registered = voter.get("registered", False)
        criminal_record = voter.get("criminal_record", False)
    except KeyError as e:
        return f"Missing required attribute: {e}"
    except TypeError:
        return "Invalid data type for voter attributes"

    if not isinstance(age, (int, float)):
        return "Age must be a number"
    if age < 18:
        return "ineligible_too_young"
    if not citizenship:
        return "ineligible_not_citizen"
    if not registered:
        return "ineligible_not_registered"
    if criminal_record:
        return "ineligible_criminal_record"

    return "eligible"

if __name__ == '__main__':
    sample_voter = {
        "age": 25,
        "citizenship": True,
        "registered": True,
        "criminal_record": False
    }
    print(check_voter_eligibility(sample_voter))

    young_voter = {
        "age": 16,
        "citizenship": True,
        "registered": True,
        "criminal_record": False
    }
    print(check_voter_eligibility(young_voter))

    non_citizen = {
        "age": 30,
        "citizenship": False,
        "registered": True,
        "criminal_record": False
    }
    print(check_voter_eligibility(non_citizen))

    missing_age = {
        "citizenship": True,
        "registered": True
    }
    print(check_voter_eligibility(missing_age))

    criminal_voter = {
        "age": 40,
        "citizenship": True,
        "registered": True,
        "criminal_record": True
    }
    print(check_voter_eligibility(criminal_voter))