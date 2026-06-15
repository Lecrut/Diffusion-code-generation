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
    test_string_1 = "10,20,30,40"
    result_1 = calculate_average(test_string_1)
    print(f"Average of '{test_string_1}': {result_1}")
    test_string_2 = "5.5,10.5,15.0"
    result_2 = calculate_average(test_string_2)
    print(f"Average of '{test_string_2}': {result_2}")
    test_string_3 = "1,2,three,4"
    result_3 = calculate_average(test_string_3)
    print(f"Average of '{test_string_3}': {result_3}")
    test_string_4 = ""
    result_4 = calculate_average(test_string_4)
    print(f"Average of '{test_string_4}': {result_4}")
    test_string_5 = "100"
    result_5 = calculate_average(test_string_5)
    print(f"Average of '{test_string_5}': {result_5}")