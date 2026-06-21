def is_eligible(age):
    if age < 0:
        return False
    return age >= 18

if __name__ == '__main__':
    sample_ages = [17, 18, 19, -5, 25]
    for age in sample_ages:
        result = is_eligible(age)
        print(f"Age {age}: {result}")