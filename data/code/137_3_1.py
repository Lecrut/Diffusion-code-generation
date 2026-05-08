def classify_numbers(numbers):
    results = []
    for number in numbers:
        if number > 0:
            result = "Positive"
        elif number < 0:
            result = "Negative"
        else:
            result = "Zero"
        results.append(result)
    return results
if __name__ == '__main__':
    sample_list = [10, -5, 0, 3.14, -100, 0.0]
    classification = classify_numbers(sample_list)
    for number, classification_result in zip(sample_list, classification):
        print(f"{number}: {classification_result}")