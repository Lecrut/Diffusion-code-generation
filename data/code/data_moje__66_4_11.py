def km_to_m(km):
    return round(km * 1000, 10)

if __name__ == '__main__':
    print(km_to_m(1.5))
    print(km_to_m(0.001))
    print(km_to_m(123.456789012345))
    print(km_to_m(-5.25))
    print(km_to_m(0.0))