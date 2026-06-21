def min_integer(mixed_list):
    return int(min(float(item) for item in mixed_list))

if __name__ == '__main__':
    sample_values = [3, 5.5, '2', -1, '0']
    print(min_integer(sample_values))