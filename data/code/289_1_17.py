def miles_to_cm(miles):
    conversion_factor = 160934
    cm_per_meter = 100
    total_cm = miles * conversion_factor * cm_per_meter
    return total_cm
if __name__ == '__main__':
    distance_in_miles = 5
    result = miles_to_cm(distance_in_miles)
    print(f'{distance_in_miles} miles is equal to {result} centimeters.')