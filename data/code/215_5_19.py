def find_largest(data):
    return max(data, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [-5, -10, -2, -8, -1]
    largest_value = find_largest(sample_list)
    print(largest_value)