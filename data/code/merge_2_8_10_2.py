import sys
def calculate_score(age):
    if age < 18:
        return "Minor access denied"
    elif age > 65:
        return "Senior discount applied"
    else:
        return "Standard rate applicable"
if __name__ == '__main__':
    try:
        sample_age = int("25")
        if not isinstance(sample_age, (int, float)):
            raise TypeError("Input must be a number")
        result = calculate_score(int(sample_age))
        print(f"For age {sample_age}: {result}")
    except ValueError as ve:
        print(f"Error: Invalid input - {ve}", file=sys.stderr)
        sys.exit(1)
    except TypeError as te:
        print(f"Error: Incorrect data type - {te}", file=sys.stderr)
        sys.exit(1)