def meters_to_kilometers(meters):
    if not isinstance(meters, (int, float)) or meters < 0:
        raise ValueError("Input must be a non-negative number")
    return round(meters / 1000.0, 2)

if __name__ == '__main__':
    sample_meters = 500
    try:
        result_km = meters_to_kilometers(sample_meters)
        print(f"{sample_meters} meters is equal to {result_km} kilometers")
    except ValueError as e:
        print(e)