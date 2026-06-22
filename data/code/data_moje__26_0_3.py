VOTING_AGE = 18

def is_eligible_to_vote(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= VOTING_AGE

if __name__ == '__main__':
    ages_to_check = [17, 18, 21, 100, -5, 18.0]
    for test_age in ages_to_check:
        try:
            result = is_eligible_to_vote(test_age)
            print(result)
        except (TypeError, ValueError):
            print("Invalid input")