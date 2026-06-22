def adjust_distance(distance, unit):
    factors = {
        'miles': 1.60934,
        'km': 1 / 1.60934
    }
    if unit == 'miles':
        return distance * factors['miles'], 'km'
    elif unit == 'km':
        return distance * factors['km'], 'miles'
    else:
        raise ValueError("Unsupported unit. Use 'miles' or 'km'.")

if __name__ == '__main__':
    result, new_unit = adjust_distance(10, 'miles')
    print(result, new_unit)
    result2, new_unit2 = adjust_distance(5, 'km')
    print(result2, new_unit2)