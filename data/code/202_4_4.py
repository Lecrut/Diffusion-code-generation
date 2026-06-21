def find_largest(*integers):
    return max(integers)

if __name__ == '__main__':
    sample_values = (45, 23, 67, 89, 34)
    largest_number = find_largest(*sample_values)
    print(largest_number)