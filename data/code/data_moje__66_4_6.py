def km_to_m(kilometers: float) -> float:
    return round(kilometers * 1000, 2)

if __name__ == '__main__':
    result = km_to_m(5.123)
    print(result)