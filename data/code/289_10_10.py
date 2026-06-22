def km_to_miles(kilometers):
    return round(kilometers * 0.621371, 2)

if __name__ == '__main__':
    sample_km = 100
    result_miles = km_to_miles(sample_km)
    print(f"{sample_km} kilometers is equal to {result_miles:.2f} miles.")