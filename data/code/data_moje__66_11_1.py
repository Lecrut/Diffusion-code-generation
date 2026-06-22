def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_kilometers = [1.5, 3.2, 0.75, 10.0, 42.195]
    meters = kilometers_to_meters(sample_kilometers)
    print(meters)