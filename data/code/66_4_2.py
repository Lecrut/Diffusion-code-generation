def km_to_m(kilometers: float) -> float:
    return round(kilometers * 1000, 10)

if __name__ == '__main__':
    result = km_to_m(1.2345)
    print(result)
    result = km_to_m(0.5)
    print(result)