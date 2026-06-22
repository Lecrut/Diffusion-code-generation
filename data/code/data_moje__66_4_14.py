def km_to_m(kilometers):
    return round(kilometers * 1000, 10)

if __name__ == '__main__':
    result1 = km_to_m(1.5)
    result2 = km_to_m(0.001)
    print(result1)
    print(result2)