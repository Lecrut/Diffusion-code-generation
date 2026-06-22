def convert_miles_to_feet(measurements):
    return {key: value * 5280 for key, value in measurements.items()}

if __name__ == '__main__':
    mile_data = {"distance_1": 1.5, "distance_2": 3.2, "distance_3": 0.5}
    foot_data = convert_miles_to_feet(mile_data)
    print(foot_data)