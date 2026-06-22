def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18

def main():
    test_cases = [
        (17, False),
        (18, True),
        (21, True),
        (0, False),
        (-1, "ValueError"),
        ("eighteen", "TypeError"),
        (None, "TypeError")
    ]
    for case in test_cases:
        age_input = case[0]
        expected = case[1]
        try:
            result = check_voting_eligibility(age_input)
            print(f"Age {age_input}: {result}")
        except (ValueError, TypeError) as e:
            print(f"Age {age_input}: {type(e).__name__}")

if __name__ == '__main__':
    main()