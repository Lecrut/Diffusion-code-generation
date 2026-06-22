def convert_kilometers_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    sample_values = [1, 2.5, 10, 0.5]
    result = convert_kilometers_to_meters(sample_values)
    print(result)