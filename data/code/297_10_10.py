def meters_to_kilometers(meters):
    if meters < 0:
        raise ValueError("Negative input not allowed")
    return meters / 1000.0

if __name__ == '__main__':
    sample_meters = -500
    try:
        result = meters_to_kilometers(sample_meters)
        print(result)
    except ValueError as e:
        print(e)