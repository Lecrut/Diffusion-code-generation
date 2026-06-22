def kilometers_to_meters(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number")
    return kilometers * 1000

if __name__ == '__main__':
    distance_km = 5
    distance_m = kilometers_to_meters(distance_km)
    print(distance_m)