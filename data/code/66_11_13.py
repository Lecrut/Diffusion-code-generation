def convert_km_to_m(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    km_values = [1, 5, 10, 0.5]
    meters_values = convert_km_to_m(km_values)
    print(meters_values)