def categorize_number(number: int) -> str:
    if number < 10:
        return "small"
    elif number < 100:
        return "medium"
    else:
        return "large"

if __name__ == '__main__':
    sample_numbers = [5, 42, 123]
    for num in sample_numbers:
        print(f"{num}: {categorize_number(num)}")