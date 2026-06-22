def convert_kilometers_to_meters(kilometers):
    return [km * 1000 for km in kilometers]

if __name__ == '__main__':
    sample_kilometers = [1.5, 2, 10, 0.5]
    result = convert_kilometers_to_meters(sample_kilometers)
    print(result)