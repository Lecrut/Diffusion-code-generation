def categorize_number(number: int) -> str:
    if number < 10:
        return "small"
    elif number < 100:
        return "medium"
    else:
        return "large"

if __name__ == '__main__':
    sample_value = 55
    category = categorize_number(sample_value)
    print(f"{sample_value}: {category}")