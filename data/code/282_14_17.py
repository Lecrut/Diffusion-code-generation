def calculate_total(numbers_str):
    numbers_list = [int(num) for num in numbers_str.split()]
    total = sum(numbers_list)
    return total

if __name__ == '__main__':
    sample_input = "10 20 30 40"
    result = calculate_total(sample_input)
    print(result)