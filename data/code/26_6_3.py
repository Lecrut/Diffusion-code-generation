def validate_voting_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 18:
        raise ValueError("Must be at least 18 years old")
    return True

if __name__ == '__main__':
    sample_ages = [18, 25, 17, -1, 17.9]
    for age in sample_ages:
        try:
            result = validate_voting_age(age)
            print(f"Age {age}: Eligible")
        except ValueError as e:
            print(f"Age {age}: Ineligible - {e}")
        except TypeError as e:
            print(f"Age {age}: Invalid Type - {e}")