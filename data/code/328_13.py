def calculate_string_length(input_value):
    return len(str(input_value))
if __name__ == '__main__':
    sample1 = "hello world"
    result1 = calculate_string_length(sample1)
    print(f"The length of '{sample1}' is: {result1}")
    sample2 = 12345
    result2 = calculate_string_length(sample2)
    print(f"The length of '{sample2}' (as string) is: {result2}")
    sample3 = ""
    result3 = calculate_string_length(sample3)
    print(f"The length of '{sample3}' is: {result3}")
    sample4 = "Python"
    result4 = calculate_string_length(sample4)
    print(f"The length of '{sample4}' is: {result4}")