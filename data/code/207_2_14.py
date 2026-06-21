def find_max_in_tuple(floats):
    return max(floats)

if __name__ == '__main__':
    sample_values = (10.5, 23.4, 7.8, 99.9, 5.6)
    max_value = find_max_in_tuple(sample_values)
    print(f"The maximum value in {sample_values} is {max_value}")