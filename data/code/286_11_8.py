def convert_feet_to_meters(feet):
    if not isinstance(feet, (int, float)):
        raise ValueError("Invalid input type. Must be an integer or float.")
    return feet * 0.3048

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = convert_feet_to_meters(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")