def find_largest_number(numbers):
    return max(map(int, numbers))

if __name__ == '__main__':
    sample_numbers = ['34', '123', '56', '90']
    print(find_largest_number(sample_numbers))