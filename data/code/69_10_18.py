FEET_PER_MILE = 5280.0

def miles_to_feet(miles):
    return float(miles * FEET_PER_MILE)

if __name__ == '__main__':
    print(miles_to_feet(1.0))
    print(miles_to_feet(0.25))
    print(miles_to_feet(100.0))