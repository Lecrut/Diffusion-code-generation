def find_max_number(numbers):
    if not numbers:
        raise ValueError("Input string cannot be empty")
    return max(map(int, numbers.split()))

if __name__ == '__main__':
    sample_string = "3 14 27 18 6"
    try:
        maximum = find_max_number(sample_string)
        print(maximum)
    except ValueError as e:
        print(e)