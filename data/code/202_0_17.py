MAX_NUMBER = 30

def find_max_number(numbers):
    return max(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 15]
    largest_number = find_max_number(sample_numbers)
    print(largest_number)