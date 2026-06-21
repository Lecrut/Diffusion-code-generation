def find_min_value(data_generator):
    min_value = float('inf')
    for value in data_generator:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_data = (x**2 for x in range(1000000))
    print(find_min_value(sample_data))