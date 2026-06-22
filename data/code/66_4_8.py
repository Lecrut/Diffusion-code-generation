def km_to_m(kilometers):
    return round(kilometers * 1000, 10)

if __name__ == '__main__':
    result = km_to_m(1.2345678901234)
    print(result)