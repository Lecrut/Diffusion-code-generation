def kilometers_to_miles(kilometers):
    conversion_factor = 5 / 8.0
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 16
    miles = kilometers_to_miles(sample_kilometers)
    print(miles)