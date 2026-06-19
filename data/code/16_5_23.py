def determine_positivity(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

if __name__ == '__main__':
    test_values = [10, -5, 0]
    results = [determine_positivity(value) for value in test_values]
    print(results)