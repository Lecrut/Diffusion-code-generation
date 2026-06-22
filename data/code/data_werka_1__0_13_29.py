def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

if __name__ == '__main__':
    sample_kilometers = 5.0
    converted_miles = kilometers_to_miles(sample_kilometers)
    print(converted_miles)