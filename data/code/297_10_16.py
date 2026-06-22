def meters_to_kilometers(meters):
    if not isinstance(meters, (int, float)) or meters < 0:
        raise ValueError('Input must be a non-negative number.')
    return meters / 1000.0
if __name__ == '__main__':
    print(meters_to_kilometers(1000))
    print(meters_to_kilometers(500))
    print(meters_to_kilometers(0))