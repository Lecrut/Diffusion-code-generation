def km_to_m(kilometers: float) -> float:
    meters = kilometers * 1000.0
    return round(meters, 10)

if __name__ == '__main__':
    distance_km = 5.123
    distance_m = km_to_m(distance_km)
    print(distance_m)