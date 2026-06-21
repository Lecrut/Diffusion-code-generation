def check_voter_eligibility(attributes: dict) -> dict:
    try:
        age = attributes.get('age')
        citizenship = attributes.get('citizenship', False)
        registered = attributes.get('registered', False)
        has_id = attributes.get('has_id', False)

        if age is None or not isinstance(age, (int, float)):
            return {"eligible": False, "reason": "Invalid or missing age"}
        if age < 18:
            return {"eligible": False, "reason": "Under 18 years old"}
        if not citizenship:
            return {"eligible": False, "reason": "Not a citizen"}
        if not registered:
            return {"eligible": False, "reason": "Not registered to vote"}
        if not has_id:
            return {"eligible": False, "reason": "No valid ID"}
        return {"eligible": True, "reason": "Eligible to vote"}
    except Exception as e:
        return {"eligible": False, "reason": f"Error processing attributes: {str(e)}"}

if __name__ == '__main__':
    sample_voter = {
        "age": 25,
        "citizenship": True,
        "registered": True,
        "has_id": True
    }
    result = check_voter_eligibility(sample_voter)
    print(result)

    ineligible_voter = {
        "age": 16,
        "citizenship": True,
        "registered": True,
        "has_id": True
    }
    result2 = check_voter_eligibility(ineligible_voter)
    print(result2)

    missing_data_voter = {
        "age": None,
        "citizenship": True,
        "registered": True,
        "has_id": True
    }
    result3 = check_voter_eligibility(missing_data_voter)
    print(result3)