def convert_kilometers_to_meters(kilometer_values):
    return [km * 1000 for km in kilometer_values]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2, 3.25, 10, 0.5]
    result = convert_kilometers_to_meters(sample_kilometers)
    print(result)