def kilometers_to_meters(kilometer_values):
    return [kilometer * 1000 for kilometer in kilometer_values]

if __name__ == '__main__':
    sample_kilometers = [1.0, 2.5, 0.5, 10, 0]
    result = kilometers_to_meters(sample_kilometers)
    print(result)