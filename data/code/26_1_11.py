def check_voting_eligibility(age):
    if not isinstance(age, (int, float)):
        return False
    age = int(age)
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    sample_ages = [17, 18, 25, -1, 0, 100, 17.9]
    for a in sample_ages:
        result = check_voting_eligibility(a)
        print(f"Age {a}: {result}")