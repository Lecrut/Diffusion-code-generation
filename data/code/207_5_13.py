def find_largest_number(str_numbers):
    return max(map(int, str_numbers))
if __name__ == '__main__':
    sample_values = ['3', '56', '2', '90', '1']
    largest_number = find_largest_number(sample_values)
    print(largest_number)