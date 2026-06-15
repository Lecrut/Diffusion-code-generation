def calculate_average(data_string):
    numbers = []
    for item in data_string.split(','):
        try:
            numbers.append(float(item.strip()))
        except ValueError:
            return None
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
if __name__ == '__main__':
    test_string_valid = "10,20,30,40,50"
    test_string_invalid = "10,20,thirty,40"
    test_string_empty = ""
    test_string_only_commas = ",,"
    test_string_single = "100"
    result1 = calculate_average(test_string_valid)
    print(f"Average of '{test_string_valid}': {result1}")
    result2 = calculate_average(test_string_invalid)
    print(f"Average of '{test_string_invalid}': {result2}")
    result3 = calculate_average(test_string_empty)
    print(f"Average of '{test_string_empty}': {result3}")
    result4 = calculate_average(test_string_only_commas)
    print(f"Average of '{test_string_only_commas}': {result4}")
    result5 = calculate_average(test_string_single)
    print(f"Average of '{test_string_single}': {result5}")