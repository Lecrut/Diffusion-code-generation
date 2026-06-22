def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    input_km = [1.0, 2.5, 10, 0.5]
    result = kilometers_to_meters(input_km)
    print(result)