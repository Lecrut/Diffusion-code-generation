def find_largest_number(mixed_list):
    return max(float(item) for item in mixed_list)

if __name__ == '__main__':
    sample_input = [3, 5.5, '2', 7, '8.1']
    print(find_largest_number(sample_input))