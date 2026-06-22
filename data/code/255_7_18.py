def find_max_number(numbers):
    return max(map(int, numbers.split()))

if __name__ == '__main__':
    sample_numbers = "3 5 2 8 1"
    print(find_max_number(sample_numbers))