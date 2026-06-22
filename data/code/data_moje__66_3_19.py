def convert_kilometers_to_meters(kilometer_values):
    return [value * 1000 for value in kilometer_values]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2.0, 0.75, 10, 3.14]
    result = convert_kilometers_to_meters(sample_kilometers)
    print(result)