def convert_feet_to_meters(length_feet):
    conversion_factor = 0.3048
    return length_feet * conversion_factor

if __name__ == '__main__':
    length_feet_sample = 10.0
    result_meters = convert_feet_to_meters(length_feet_sample)
    print(f"{length_feet_sample} ft converted to meters: {result_meters}")