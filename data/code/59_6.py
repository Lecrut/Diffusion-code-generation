def digit_sum(number_str):
    total = 0
    for char in number_str:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample_numbers = ["12345", "999", "0", "-42", "1000000"]
    for num in sample_numbers:
        result = digit_sum(num)
        print(result)