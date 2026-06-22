def find_max_number(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    return max(numbers)

if __name__ == '__main__':
    sample_input = "3 5 1 2 4"
    print(find_max_number(sample_input))