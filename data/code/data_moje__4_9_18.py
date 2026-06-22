def convert_distance(value, unit):
    if unit == "miles":
        return value * 1.60934
    elif unit == "kilometers":
        return value / 1.60934
    else:
        return None

if __name__ == '__main__':
    miles_value = 10.0
    result = convert_distance(miles_value, "miles")
    print(result)

    kilometers_value = 16.0934
    result2 = convert_distance(kilometers_value, "kilometers")
    print(result2)