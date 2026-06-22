def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_km = [1, 2.5, 10, 0.5, 100]
    print(kilometers_to_meters(sample_km))