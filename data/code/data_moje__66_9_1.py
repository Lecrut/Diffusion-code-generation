def convert_to_meters(kilometers_tuple):
    return tuple(map(lambda km: km * 1000, kilometers_tuple))

if __name__ == '__main__':
    kilometers = (1, 5, 10, 2.5)
    meters = convert_to_meters(kilometers)
    print(meters)