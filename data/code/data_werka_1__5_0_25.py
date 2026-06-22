def calculate_difference(length1, length2):
    try:
        diff = float(length1) - float(length2)
        return diff
    except ValueError:
        return "Error: Both inputs must be numeric."

if __name__ == '__main__':
    sample_length1 = "10.5"
    sample_length2 = "3.2"
    result = calculate_difference(sample_length1, sample_length2)
    print(result)