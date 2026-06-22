def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = 5
    miles = kilometers_to_miles(sample_kilometers)
    print(miles)