def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
if __name__ == '__main__':
    sample_input = "10 5 22 8"
    try:
        number_list = [int(x) for x in sample_input.split()]
        result = calculate_sum(number_list)
        print(result)
    except ValueError:
        print("Error: Input contained non-integer values.")