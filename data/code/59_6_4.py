def calculate_digit_sum(number_string):
    total = 0
    for char in number_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    test_values = ["12345", "987654321", "007", "-42", ""]
    for value in test_values:
        result = calculate_digit_sum(value)
        print(f"Input: '{value}', Digit Sum: {result}")