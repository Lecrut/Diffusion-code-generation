def kilometers_to_meters(kilometers_list):
    return [value * 1000 for value in kilometers_list]

if __name__ == '__main__':
    sample_values = [1.5, 2.0, 3.75, 0.5]
    result = kilometers_to_meters(sample_values)
    print(result)