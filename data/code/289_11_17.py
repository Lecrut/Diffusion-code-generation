def meters_to_feet(meters):
    try:
        return [round(m * 3.28084, 2) for m in meters]
    except TypeError:
        raise ValueError("Input must be a list of numeric values.")

if __name__ == '__main__':
    sample_meters = [10, 20, 30, 40, 50]
    result_feet = meters_to_feet(sample_meters)
    print(result_feet)