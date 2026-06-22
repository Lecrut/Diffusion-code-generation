def km_to_m(kilometers):
    return round(kilometers * 1000, 10)

if __name__ == '__main__':
    result = km_to_m(5.2)
    print(result)
    result = km_to_m(0.001)
    print(result)
    result = km_to_m(100)
    print(result)