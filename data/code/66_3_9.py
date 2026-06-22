def convert_kilometers_to_meters(kilometers_list):
    return [value * 1000 for value in kilometers_list]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2, 0.75, 10]
    result_meters = convert_kilometers_to_meters(sample_kilometers)
    print(result_meters)