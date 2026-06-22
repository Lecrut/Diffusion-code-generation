def convert_kilometers_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    input_values = [1, 5, 10, 0.5, 100]
    result = convert_kilometers_to_meters(input_values)
    print(result)