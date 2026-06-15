def calculate_mean(input_string):
    numbers = []
    try:
        parts = input_string.split()
        for part in parts:
            numbers.append(float(part))
        if not numbers:
            return None
        return sum(numbers) / len(numbers)
    except ValueError:
        return None
if __name__ == '__main__':
    test_string_1 = "10 20 30 40"
    result_1 = calculate_mean(test_string_1)
    print(f"Input: '{test_string_1}', Mean: {result_1}")
    test_string_2 = "5.5 10.5 15.0"
    result_2 = calculate_mean(test_string_2)
    print(f"Input: '{test_string_2}', Mean: {result_2}")
    test_string_3 = "1 2 three 4"
    result_3 = calculate_mean(test_string_3)
    print(f"Input: '{test_string_3}', Mean: {result_3}")
    test_string_4 = ""
    result_4 = calculate_mean(test_string_4)
    print(f"Input: '{test_string_4}', Mean: {result_4}")