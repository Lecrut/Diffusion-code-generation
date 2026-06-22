def find_max_number(numbers_str):
    numbers = list(map(int, numbers_str.split()))
    return max(numbers)

if __name__ == '__main__':
    result = find_max_number("3 5 2 8 1")
    print(result)