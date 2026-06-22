def kilometers_to_miles(kilometers):
    conversion_factor = 5 / 8
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 10
    miles = kilometers_to_miles(sample_kilometers)
    print(miles)