def sum_space_separated_numbers(input_string):
    total_sum = 0
    parts = input_string.split()
    for part in parts:
        try:
            total_sum += int(part)
        except ValueError:
            pass
    return total_sum
if __name__ == '__main__':
    test_string1 = "10 20 30"
    result1 = sum_space_separated_numbers(test_string1)
    print(f"Input: '{test_string1}', Sum: {result1}")
    test_string2 = "5 15 hello 25"
    result2 = sum_space_separated_numbers(test_string2)
    print(f"Input: '{test_string2}', Sum: {result2}")
    test_string3 = "1.5 2.5 3"
    result3 = sum_space_separated_numbers(test_string3)
    print(f"Input: '{test_string3}', Sum: {result3}")
    test_string4 = "abc 100 def"
    result4 = sum_space_separated_numbers(test_string4)
    print(f"Input: '{test_string4}', Sum: {result4}")
    test_string5 = ""
    result5 = sum_space_separated_numbers(test_string5)
    print(f"Input: '{test_string5}', Sum: {result5}")