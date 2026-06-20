def categorize_number(value: int) -> str:
    if -10 <= value < 0:
        return "Small"
    elif 0 <= value < 10:
        return "Medium"
    elif value >= 10:
        return "Large"
    else:
        raise ValueError("Invalid input: Value must be an integer.")

if __name__ == '__main__':
    sample_values = [-5, 2, 10, 15]
    for value in sample_values:
        try:
            category = categorize_number(value)
            print(f"{value}: {category}")
        except ValueError as e:
            print(e)