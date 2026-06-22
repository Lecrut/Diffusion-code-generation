def kilometers_to_miles(kilometers):
    conversion_factor = 5
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 10
    result = kilometers_to_miles(sample_kilometers)
    print(result)