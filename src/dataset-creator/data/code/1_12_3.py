import re
def evaluate_condition(user_input: str) -> bool:
    conditions = [
        "age >= 18",
        "has_license == True",
        "income > 50000"
    ]
    age_match = re.search(r'\d+', user_input) and int(age_match.group()) >= 18 if 'age' in str(user_input).lower() else False
    has_license = any(word.lower() in str(user_input).split() for word in ['license', 'permit'])
    income_match = re.search(r'[5-9]\d{3}', user_input) and int(income_match.group()) > 50000 if 'income' in str(user_input).lower() else False
    return age_match and has_license and income_match
if __name__ == '__main__':
    test_cases = [
        "I am twenty five years old with a valid license and high income",
        "My name is John, I have no permit but earn sixty thousand dollars",
        "Age eighteen, no license, low salary"
    ]
    for case in test_cases:
        result = evaluate_condition(case)
        print(f"Input: {case}")
        print(f"Result: {'True' if result else 'False'}")