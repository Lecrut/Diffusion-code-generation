def convert_km_to_m(kilometers):
    if not isinstance(kilometers, (int, float)):
        raise ValueError("Input must be a number")
    if kilometers < 0:
        raise ValueError("Input must be a non-negative number")
    return kilometers * 1000

if __name__ == '__main__':
    print(convert_km_to_m(5))
    print(convert_km_to_m(0.5))
    print(convert_km_to_m(0))