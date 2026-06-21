def is_eligible_to_vote(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18

if __name__ == '__main__':
    test_ages = [17, 18, 19, -5, 25, 0]
    for age in test_ages:
        try:
            result = is_eligible_to_vote(age)
            print(f"Age {age}: {result}")
        except ValueError as e:
            print(f"Age {age}: Error - {e}")