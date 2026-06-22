def find_min(values):
    min_value = values[0]
    for value in values:
        if value < min_value:
            min_value = value
    return min_value

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, -2.1, 0.0]
    print(find_min(sample_values))