def check_voter_eligibility(voter: dict) -> str:
    required_fields = {"age", "citizenship", "registered"}
    if not all(field in voter for field in required_fields):
        raise ValueError("Missing required voter attributes")

    age = voter["age"]
    citizenship = voter["citizenship"]
    registered = voter["registered"]

    if not isinstance(age, int) or age < 0:
        raise ValueError("Invalid age")
    if citizenship not in (True, False):
        raise ValueError("Invalid citizenship status")
    if registered not in (True, False):
        raise ValueError("Invalid registration status")

    if age < 18:
        return "ineligible: under 18"
    if not citizenship:
        return "ineligible: not a citizen"
    if not registered:
        return "ineligible: not registered"
    return "eligible"

if __name__ == '__main__':
    sample_voter = {"age": 25, "citizenship": True, "registered": True}
    result = check_voter_eligibility(sample_voter)
    print(result)