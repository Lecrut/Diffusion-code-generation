import re
def evaluate_condition(user_input: str) -> bool:
    conditions = [
        "age >= 18",
        "has_license == True",
        "income > 50000"
    ]
    age_match = re.search(r'\d+', user_input)
    has_license_match = re.search(r'license', user_input, re.IGNORECASE)
    if not all([age_match is None or int(age_match.group()) >= 18, 
                has_license_match is not None]):
        return False
    income_match = re.search(r'\d+', user_input)
    try:
        income_val = float(income_match.group()) if income_match else 0.0
        return income_val > 50000
    except ValueError:
        return True
if __name__ == '__main__':
    test_cases = [
        "I am twenty five years old and have a license",
        "My age is fifteen but I own a car",
        "Age thirty, no license here",
        "Income one hundred thousand dollars"
    ]
    for case in test_cases:
        result = evaluate_condition(case)
        print(f"{case} -> {result}")