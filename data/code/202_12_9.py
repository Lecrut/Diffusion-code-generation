def find_largest_number(mixed_numbers):
    return max(map(float, mixed_numbers))

if __name__ == '__main__':
    sample_input = [3, 5.5, '2', 8, '9.1']
    print(find_largest_number(sample_input))