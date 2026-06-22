def convert_kilometers_to_meters(kilometer_values):
    return [km * 1000 for km in kilometer_values]

if __name__ == '__main__':
    km_values = [1.5, 2, 3.75, 10]
    result = convert_kilometers_to_meters(km_values)
    print(result)