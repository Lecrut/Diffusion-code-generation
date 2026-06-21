def find_max_element(*args):
    return max(args)

if __name__ == '__main__':
    sample_values = (12, 45, 78, 3, 67)
    largest_value = find_max_element(*sample_values)
    print(largest_value)