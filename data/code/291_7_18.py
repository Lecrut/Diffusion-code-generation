def convert_to_miles(kilometers):
    return kilometers * 0.621371

def convert_to_kilometers(miles):
    return miles / 0.621371

def compare_measures(value1, unit1, value2, unit2):
    if unit1 == 'miles' and unit2 == 'kilometers':
        value1_converted = value1
        value2_converted = convert_to_kilometers(value2)
    elif unit1 == 'kilometers' and unit2 == 'miles':
        value1_converted = convert_to_miles(value1)
        value2_converted = value2
    else:
        raise ValueError("Unsupported units. Please use 'miles' or 'kilometers'.")

    if value1_converted > value2_converted:
        return f"{value1} {unit1} is greater than {value2} {unit2}"
    elif value1_converted < value2_converted:
        return f"{value1} {unit1} is less than {value2} {unit2}"
    else:
        return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == '__main__':
    result = compare_measures(5, 'miles', 8.0467, 'kilometers')
    print(result)