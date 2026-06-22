def classify_number(value):
    result = None
    if value > 0:
        result = "positive"
    elif value < 0:
        result = "negative"
    else:
        result = "zero"
    return result

if __name__ == '__main__':
    sample_values = [15.5, -20.0, 0]
    for val in sample_values:
        classification = classify_number(val)
        print(classification)