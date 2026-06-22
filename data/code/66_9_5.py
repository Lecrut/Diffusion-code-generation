def convert_kilometers_to_meters(kilometers):
    return map(lambda km: km * 1000, kilometers)

if __name__ == '__main__':
    kilometers_tuple = (1, 5, 10, 100)
    meters_tuple = tuple(convert_kilometers_to_meters(kilometers_tuple))
    print(meters_tuple)