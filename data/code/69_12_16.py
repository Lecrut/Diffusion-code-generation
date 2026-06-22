def miles_to_feet_calc(miles: float) -> float:
    return miles * 5280

if __name__ == '__main__':
    result = miles_to_feet_calc(2.0)
    print(result)