def convert_kilometers_to_meters(kilometer_values):
    return [km * 1000 for km in kilometer_values]

if __name__ == '__main__':
    kilometers = [1, 5.5, 10, 0, 100.5]
    meters = convert_kilometers_to_meters(kilometers)
    print(meters)