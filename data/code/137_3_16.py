def categorize_number(number: int) -> str:
    if number < 10:
        return "small"
    elif number < 100:
        return "medium"
    else:
        return "large"

if __name__ == '__main__':
    sample_value = 75
    category = categorize_number(sample_value)
    print(f"The number {sample_value} is categorized as '{category}'.")