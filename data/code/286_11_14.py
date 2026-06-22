CONVERSION_FACTOR = 0.3048

def feet_to_meters(feet):
    return feet * CONVERSION_FACTOR

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = feet_to_meters(length_feet)
    print(f"{length_feet} ft converted to meters: {result_meters}")