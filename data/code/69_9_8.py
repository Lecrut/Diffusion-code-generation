def convert_miles_to_feet(data):
    return {key: value * 5280 for key, value in data.items()}

if __name__ == '__main__':
    input_data = {"distance_a": 1.5, "distance_b": 2.0}
    result = convert_miles_to_feet(input_data)
    print(result)