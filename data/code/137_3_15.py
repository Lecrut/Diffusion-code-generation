SMALL_THRESHOLD = 10
MEDIUM_THRESHOLD = 50

def categorize_number(number: int) -> str:
    if number < -SMALL_THRESHOLD:
        return "Very Negative"
    elif -SMALL_THRESHOLD <= number < SMALL_THRESHOLD:
        return "Small"
    elif SMALL_THRESHOLD <= number < MEDIUM_THRESHOLD:
        return "Medium"
    else:
        return "Large"

if __name__ == '__main__':
    sample_number = 45
    category = categorize_number(sample_number)
    print(f"{sample_number}: {category}")