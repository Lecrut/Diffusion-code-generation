def feet_to_meters(feet):
    conversion_factor = 0.3048
    meters = feet * conversion_factor
    return meters

if __name__ == '__main__':
    sample_feet = 15.0
    result_meters = feet_to_meters(sample_feet)
    print(f"{sample_feet} ft converted to meters: {result_meters}")