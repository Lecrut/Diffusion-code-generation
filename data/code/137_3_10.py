def classify_number(number: int) -> str:
    if -100 <= number < -10:
        return "Small Negative"
    elif -9 <= number < 0:
        return "Medium Negative"
    elif 1 <= number < 10:
        return "Small Positive"
    elif 10 <= number < 100:
        return "Medium Positive"
    else:
        return "Large"

if __name__ == '__main__':
    sample_number = 42
    classification = classify_number(sample_number)
    print(f"{sample_number}: {classification}")