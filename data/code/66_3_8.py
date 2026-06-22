def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    km_values = [1, 5, 10, 0.5]
    meters = kilometers_to_meters(km_values)
    print(meters)