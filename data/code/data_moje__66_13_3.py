convert = lambda km: 1000 * km if km is not None else 0

if __name__ == '__main__':
    sample_input = 5
    result = convert(sample_input)
    print(result)