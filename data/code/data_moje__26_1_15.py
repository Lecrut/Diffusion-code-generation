def is_eligible_to_vote(age):
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    test_ages = [17, 18, 19, 25, -5, 0, 100]
    for age in test_ages:
        result = is_eligible_to_vote(age)
        print(f"Age {age}: Eligible = {result}")