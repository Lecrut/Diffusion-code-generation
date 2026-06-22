def check_voting_eligibility(age):
    if age < 0:
        return "Invalid age: age cannot be negative."
    if age >= 18:
        return f"Eligible to vote. Age: {age}"
    return f"Not eligible to vote. Age: {age}"

if __name__ == '__main__':
    sample_ages = [17, 18, 25, -5, 0, 100]
    for age in sample_ages:
        result = check_voting_eligibility(age)
        print(f"Input: {age} -> {result}")