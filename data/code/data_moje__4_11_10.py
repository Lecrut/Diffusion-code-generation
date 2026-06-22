def adjust_distance(distance, unit_type):
    if unit_type == "miles":
        conversion_factor = 1.60934
        adjusted = distance * conversion_factor
        return adjusted, conversion_factor
    elif unit_type == "km":
        conversion_factor = 0.621371
        adjusted = distance * conversion_factor
        return adjusted, conversion_factor
    else:
        raise ValueError("Unsupported unit type. Use 'miles' or 'km'.")

if __name__ == '__main__':
    sample_distance = 10
    sample_unit = "miles"
    result, factor = adjust_distance(sample_distance, sample_unit)
    print(result)
    print(factor)

    sample_distance2 = 10
    sample_unit2 = "km"
    result2, factor2 = adjust_distance(sample_distance2, sample_unit2)
    print(result2)
    print(factor2)