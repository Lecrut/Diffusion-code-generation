def get_voter_eligibility(voter_attributes: dict) -> dict:
    age = voter_attributes.get("age")
    citizenship = voter_attributes.get("citizenship")
    registered = voter_attributes.get("registered")

    if age is None or citizenship is None or registered is None:
        raise ValueError("Voter attributes must include 'age', 'citizenship', and 'registered' keys.")

    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    if not isinstance(citizenship, str):
        raise TypeError("Citizenship must be a string.")
    if not isinstance(registered, bool):
        raise TypeError("Registered must be a boolean.")

    is_citizen = citizenship.lower() == "citizen"
    is_of_age = age >= 18
    is_registered = registered is True

    eligible = is_citizen and is_of_age and is_registered

    return {
        "eligible": eligible,
        "reason": "" if eligible else (
            "Not a citizen" if not is_citizen else (
                "Under 18" if not is_of_age else "Not registered"
            )
        )
    }

if __name__ == '__main__':
    result = get_voter_eligibility({"age": 20, "citizenship": "citizen", "registered": True})
    print(result)
    
    ineligible_result = get_voter_eligibility({"age": 17, "citizenship": "citizen", "registered": True})
    print(ineligible_result)
    
    ineligible_citizen_result = get_voter_eligibility({"age": 20, "citizenship": "resident", "registered": True})
    print(ineligible_citizen_result)
    
    unregistered_result = get_voter_eligibility({"age": 20, "citizenship": "citizen", "registered": False})
    print(unregistered_result)