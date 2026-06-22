def meter_values(kilometers):
    for km in kilometers:
        yield km * 1000

if __name__ == '__main__':
    sample_kilometers = [1, 2, 5, 10, 25]
    for value in meter_values(sample_kilometers):
        print(value)