def kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2.0, 3.75, 10, 0.125]
    result = kilometers_to_meters(sample_kilometers)
    print(result)