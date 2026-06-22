def km_to_meters(kilometers):
    return [k * 1000 for k in kilometers]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2.0, 3.75, 10.25]
    result = km_to_meters(sample_kilometers)
    print(result)