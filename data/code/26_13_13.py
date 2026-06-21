from typing import Any

def check_voter_eligibility(attributes: dict[str, Any]) -> bool:
    age = attributes.get("age")
    citizenship = attributes.get("citizenship")
    registered = attributes.get("registered")

    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if not isinstance(citizenship, str):
        raise TypeError("Citizenship must be a string")
    if not isinstance(registered, bool):
        raise TypeError("Registration status must be a boolean")

    if age < 18:
        return False
    if citizenship.lower() != "citizen":
        return False
    if not registered:
        return False

    return True

if __name__ == "__main__":
    voter1: dict[str, Any] = {
        "age": 25,
        "citizenship": "Citizen",
        "registered": True,
    }
    voter2: dict[str, Any] = {
        "age": 17,
        "citizenship": "Citizen",
        "registered": True,
    }
    voter3: dict[str, Any] = {
        "age": 30,
        "citizenship": "Alien",
        "registered": True,
    }
    voter4: dict[str, Any] = {
        "age": 40,
        "citizenship": "Citizen",
        "registered": False,
    }

    print(check_voter_eligibility(voter1))
    print(check_voter_eligibility(voter2))
    print(check_voter_eligibility(voter3))
    print(check_voter_eligibility(voter4))