LARGEST_NUMBERS = [3.14, 2.71, 1.41, 9.81, 6.28]

def find_largest_number(numbers):
    return max(numbers)

if __name__ == '__main__':
    largest = find_largest_number(LARGEST_NUMBERS)
    print(largest)