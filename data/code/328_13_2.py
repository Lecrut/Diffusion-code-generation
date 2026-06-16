def calculate_string_length(input_value):
    return len(str(input_value))
if __name__ == '__main__':
    sample1 = "hello world"
    length1 = calculate_string_length(sample1)
    print(f"The length of '{sample1}' is: {length1}")
    sample2 = 12345
    length2 = calculate_string_length(sample2)
    print(f"The length of '{sample2}' (as string) is: {length2}")
    sample3 = ""
    length3 = calculate_string_length(sample3)
    print(f"The length of '{sample3}' is: {length3}")
    sample4 = "Python"
    length4 = calculate_string_length(sample4)
    print(f"The length of '{sample4}' is: {length4}")