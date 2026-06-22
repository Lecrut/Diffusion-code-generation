def meters_to_kilometers(meters):
    if meters < 0:
        raise ValueError("Negative input is not allowed")
    return meters / 1000

if __name__ == '__main__':
    print(meters_to_kilometers(500))
    try:
        print(meters_to_kilometers(-100))
    except ValueError as e:
        print(e)