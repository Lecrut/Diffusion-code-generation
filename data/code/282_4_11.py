def calculate_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == '__main__':
    sample_list = [3, 7, 14, 2]
    result = calculate_total(sample_list)
    print(f"The total of {sample_list} is: {result}")