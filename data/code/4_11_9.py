def adjust_distance(value, unit):
    if unit == 'miles':
        factor = 1.60934
        return value * factor, 'km'
    elif unit == 'km':
        factor = 0.621371
        return value * factor, 'miles'
    else:
        raise ValueError("Unit must be 'miles' or 'km'")

if __name__ == '__main__':
    miles = 10
    km_value, km_unit = adjust_distance(miles, 'miles')
    print(km_value, km_unit)
    kilometers = 50
    miles_value, miles_unit = adjust_distance(kilometers, 'km')
    print(miles_value, miles_unit)