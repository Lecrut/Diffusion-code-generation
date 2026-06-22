def kilometers_to_miles(kilometers: float) -> float:
    return kilometers * 5

if __name__ == '__main__':
    distance_km = 10
    distance_mi = kilometers_to_miles(distance_km)
    print(distance_mi)