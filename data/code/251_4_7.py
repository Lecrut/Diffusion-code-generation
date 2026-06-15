def find_largest_number(input_string):
    numbers = []
    for item in input_string.split(','):
        item = item.strip()
        if item:
            try:
                numbers.append(float(item))
            except ValueError:
                pass
    if not numbers:
        return None
    return max(numbers)
if __name__ == '__main__':
    test_string_1 = "10,5,22,8"
    print(f"Input: '{test_string_1}', Largest: {find_largest_number(test_string_1)}")
    test_string_2 = "3.14,1.618,2.718"
    print(f"Input: '{test_string_2}', Largest: {find_largest_number(test_string_2)}")
    test_string_3 = "apple,banana,100,orange"
    print(f"Input: '{test_string_3}', Largest: {find_largest_number(test_string_3)}")
    test_string_4 = "7,abc,4,9"
    print(f"Input: '{test_string_4}', Largest: {find_largest_number(test_string_4)}")
    test_string_5 = ""
    print(f"Input: '{test_string_5}', Largest: {find_largest_number(test_string_5)}")
    test_string_6 = "50"
    print(f"Input: '{test_string_6}', Largest: {find_largest_number(test_string_6)}")