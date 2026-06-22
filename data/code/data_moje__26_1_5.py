def check_voting_eligibility(age):
    if not isinstance(age, int):
        return "Invalid input: Age must be an integer."
    if age < 0:
        return "Invalid input: Age cannot be negative."
    if age < 18:
        return "Not eligible to vote."
    return "Eligible to vote."

if __name__ == '__main__':
    test_ages = [19, 17, 0, -5, "20"]
    for age in test_ages:
        print(check_voting_eligibility(age))