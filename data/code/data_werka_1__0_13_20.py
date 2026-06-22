def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

if __name__ == '__main__':
    sample_kilometers = 5
    result = kilometers_to_miles(sample_kilometers)
    print(result)