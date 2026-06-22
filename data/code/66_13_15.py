MULTIPLIER = 1000

convert_km_to_m = lambda kilometers: kilometers * MULTIPLIER

if __name__ == '__main__':
    print(convert_km_to_m(5))