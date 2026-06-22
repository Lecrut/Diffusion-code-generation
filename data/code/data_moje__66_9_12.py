def kilometers_to_meters(kilometers):
    return map(lambda km: km * 1000, kilometers)

if __name__ == '__main__':
    km_values = (1.5, 2.0, 3.75, 10)
    meters = kilometers_to_meters(km_values)
    print(list(meters))