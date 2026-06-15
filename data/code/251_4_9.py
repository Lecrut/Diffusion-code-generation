def find_largest_number(input_string):
    numbers = []
    for item in input_string.split(','):
        try:
            number = float(item.strip())
            numbers.append(number)
        except ValueError:
            continue
    if not numbers:
        return None
    return max(numbers)
if __name__ == '__main__':
    test_string_1 = "10,5,22,8"
    result_1 = find_largest_number(test_string_1)
    print(f"Input: '{test_string_1}', Largest Number: {result_1}")
    test_string_2 = "3.5,1.2,9.9"
    result_2 = find_largest_number(test_string_2)
    print(f"Input: '{test_string_2}', Largest Number: {result_2}")
    test_string_3 = "a,b,10,c"
    result_3 = find_largest_number(test_string_3)
    print(f"Input: '{test_string_3}', Largest Number: {result_3}")
    test_string_4 = "50"
    result_4 = find_largest_number(test_string_4)
    print(f"Input: '{test_string_4}', Largest Number: {result_4}")
    test_string_5 = ""
    result_5 = find_largest_number(test_string_5)
    print(f"Input: '{test_string_5}', Largest Number: {result_5}")