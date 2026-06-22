def compare_miles_to_kilometers(miles, kilometers):
    miles_to_km = 1.60934
    km_to_miles = 1 / miles_to_km
    
    if miles > kilometers * km_to_miles:
        return "Miles are greater"
    elif miles < kilometers * km_to_miles:
        return "Kilometers are greater"
    else:
        return "Both measures are equal"

if __name__ == '__main__':
    print(compare_miles_to_kilometers(5, 8))