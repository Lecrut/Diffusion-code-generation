def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_km = [1.5, 2, 3.14, 0, 100]
    result = kilometers_to_meters(sample_km)
    print(result)