def find_largest_number(numbers):
    return max(map(int, numbers))

if __name__ == '__main__':
    sample_numbers = ["3", "54", "23", "98"]
    print(find_largest_number(sample_numbers))