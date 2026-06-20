def kilometers_to_miles(kilometers):
    conversion_factor = 5
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_km_values = [1, 10, 100, 5]
    for km in sample_km_values:
        miles = kilometers_to_miles(km)
        print(miles)