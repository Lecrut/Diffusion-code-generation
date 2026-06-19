def adjust_distance(distance, unit):
    if unit == 'miles':
        return distance * 1.60934, 'km'
    elif unit == 'km':
        return distance / 1.60934, 'miles'
    else:
        raise ValueError("Unsupported unit type")

if __name__ == '__main__':
    sample_distance = 5
    sample_unit = 'miles'
    adjusted_distance, new_unit = adjust_distance(sample_distance, sample_unit)
    print(f"{sample_distance} {sample_unit} is equal to {adjusted_distance} {new_unit}")