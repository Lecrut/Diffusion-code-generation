def kilometers_to_miles(kilometers):
    conversion_factor = 5.0 / 8.0
    return kilometers * conversion_factor

if __name__ == '__main__':
    sample_kilometers = [10, 20, 30]
    for km in sample_kilometers:
        miles = kilometers_to_miles(km)
        print(f"{km} kilometers is {miles} miles")