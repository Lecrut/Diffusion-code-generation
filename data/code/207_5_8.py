def find_largest_number(string_numbers):
    return max(map(int, string_numbers))

if __name__ == '__main__':
    sample_values = ['3', '56', '23', '89']
    print(find_largest_number(sample_values))