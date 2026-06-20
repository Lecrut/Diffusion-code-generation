def is_negative(number):
    NEGATIVE_THRESHOLD = 0
    return number < NEGATIVE_THRESHOLD

if __name__ == '__main__':
    sample_numbers = [-15, 42, 0]
    results = [is_negative(num) for num in sample_numbers]
    print(f"Sample numbers: {sample_numbers}")
    print(f"Are they negative? {results}")