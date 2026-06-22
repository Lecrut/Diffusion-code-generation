def convert_length(length_feet):
    return length_feet * 0.3048

if __name__ == '__main__':
    length_feet = 10.0
    result_meters = convert_length(length_feet)
    print(f"10.0 ft converted to meters: {result_meters}")