import sys
def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)):
            return False
    return True
def filter_negative_numbers(input_data):
    non_negatives = []
    negatives_found = 0
    for value in input_data:
        if value < 0:
            negatives_found += 1
        else:
            non_negatives.append(value)
    return non_negatives, negatives_found
def main():
    sample_list = [3.5, -24, 789, 0, -666]
    if not validate_input(sample_list):
        print("Invalid input data.")
        sys.exit(1)
    filtered_result, count = filter_negative_numbers(sample_list)
    print(f"Filtered list: {filtered_result}")
    print(f"Number of negative values found: {count}")
if __name__ == '__main__':
    main()