def meters_to_kilometers(meters):
    return round(meters / 1000.0, 2)

if __name__ == '__main__':
    print(meters_to_kilometers(500))
    print(meters_to_kilometers(1234))