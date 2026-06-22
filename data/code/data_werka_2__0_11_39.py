def kilometers_to_miles(kilometers):
    conversion_factor = 5
    miles = kilometers * conversion_factor
    return miles

if __name__ == '__main__':
    sample_kilometers = 20
    distance_in_miles = kilometers_to_miles(sample_kilometers)
    print(distance_in_miles)