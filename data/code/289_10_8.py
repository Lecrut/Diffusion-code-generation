def km_to_miles(kilometers):
    return round(kilometers * 0.621371, 2)
if __name__ == '__main__':
    print(km_to_miles(5))
    print(km_to_miles(10))
    print(km_to_miles(1.5))