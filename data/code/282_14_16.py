def calculate_total(numbers_str):
    numbers_list = list(map(int, numbers_str.split()))
    total = sum(numbers_list)
    return total

if __name__ == '__main__':
    sample_input = "1 2 3 4 5"
    result = calculate_total(sample_input)
    print(result)