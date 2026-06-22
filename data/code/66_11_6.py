def kilometers_to_meters(kilometers_list):
    return [km * 1000 for km in kilometers_list]

if __name__ == '__main__':
    sample_kilometers = [1.0, 2.5, 10.0, 0.5, 100.0]
    result = kilometers_to_meters(sample_kilometers)
    print(result)