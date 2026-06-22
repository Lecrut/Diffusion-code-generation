def determine_the_largest_number_present_compare(num1, num2):
    return max(num1, num2)

if __name__ == '__main__':
    sample_num1 = 45.67
    sample_num2 = 89.34
    result = determine_the_largest_number_present_compare(sample_num1, sample_num2)
    print(f"The largest number between {sample_num1} and {sample_num2} is: {result}")