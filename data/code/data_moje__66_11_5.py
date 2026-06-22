def convert_kilometers_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    km_values = [1, 2.5, 10, 0.1]
    meters_values = convert_kilometers_to_meters(km_values)
    print(meters_values)