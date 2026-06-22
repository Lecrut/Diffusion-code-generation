def adjust_distance(distance, unit):
    if unit == 'miles':
        return distance * 1.60934, 'km'
    elif unit == 'km':
        return distance / 1.60934, 'miles'
    else:
        raise ValueError("Invalid unit type. Use 'miles' or 'km'.")

if __name__ == '__main__':
    sample_distance = 5
    sample_unit = 'miles'
    adjusted_value, new_unit = adjust_distance(sample_distance, sample_unit)
    print(f"{sample_distance} {sample_unit} is equal to {adjusted_value:.2f} {new_unit}")