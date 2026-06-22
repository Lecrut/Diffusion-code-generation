def kilometers_to_miles(kilometers):
    conversion_factor = 0.621371
    miles = kilometers * conversion_factor
    return miles

if __name__ == '__main__':
    sample_kilometers = 5.0
    sample_miles = kilometers_to_miles(sample_kilometers)
    print(f"{sample_kilometers} kilometers is equal to {sample_miles} miles.")