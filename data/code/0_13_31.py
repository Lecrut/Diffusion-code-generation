def kilometers_to_miles(kilometers):
    conversion_factor = 5 / 8
    return kilometers * conversion_factor
if __name__ == '__main__':
    sample_km_values = [10, 20, 30]
    for km in sample_km_values:
        miles = kilometers_to_miles(km)
        print(f'{km} kilometers is {miles} miles')