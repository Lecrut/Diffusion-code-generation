def convert_to_meters(kilometers):
    return map(lambda km: km * 1000, kilometers)

if __name__ == '__main__':
    kilometers_tuple = (1, 2, 3, 4, 5)
    meters_tuple = tuple(convert_to_meters(kilometers_tuple))
    print(meters_tuple)