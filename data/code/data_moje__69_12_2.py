def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280.0

if __name__ == '__main__':
    sample_miles = 1.0
    print(miles_to_feet_calc(sample_miles))
    sample_miles_2 = 2.5
    print(miles_to_feet_calc(sample_miles_2))
    sample_miles_3 = 0.0
    print(miles_to_feet_calc(sample_miles_3))