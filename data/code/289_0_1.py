import sys
def km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
if __name__ == '__main__':
    sample_distance_km = 10
    result_miles = km_to_miles(sample_distance_km)
    print(f"Input distance in kilometers: {sample_distance_km}")
    print(f"Converted distance in miles: {result_miles}")