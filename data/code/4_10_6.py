import sys
def convert_distance(distance, factor):
    return distance * factor
if __name__ == '__main__':
    miles = 100.0
    conversion_factor = 1.60934
    kilometers = convert_distance(miles, conversion_factor)
    print(f"Miles: {miles}")
    print(f"Conversion Factor (Miles to Km): {conversion_factor}")
    print(f"Kilometers: {kilometers}")