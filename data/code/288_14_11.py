def is_temperature_in_range(temp, min_temp, max_temp):
    if not all(isinstance(x, (int, float)) for x in [temp, min_temp, max_temp]):
        return False
    if min_temp > max_temp:
        raise ValueError("Minimum temperature cannot be greater than maximum temperature.")
    return min_temp <= temp <= max_temp

if __name__ == '__main__':
    print(is_temperature_in_range(20, 15, 25))
    print(is_temperature_in_range(30, 20, 25))
    try:
        print(is_temperature_in_range('a', 15, 25))
    except ValueError as e:
        print(e)
    try:
        print(is_temperature_in_range(20, 25, 15))
    except ValueError as e:
        print(e)