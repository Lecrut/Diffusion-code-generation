def is_temperature_in_range(temp, min_temp, max_temp):
    if not (isinstance(temp, (int, float)) and isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float))):
        return False
    if min_temp > max_temp:
        return False
    return min_temp <= temp <= max_temp
if __name__ == '__main__':
    print(is_temperature_in_range(20, 15, 25))
    print(is_temperature_in_range(-5, -10, -3))
    print(is_temperature_in_range(30, 25, 30))
    print(is_temperature_in_range('20', 15, 25))
    print(is_temperature_in_range(20, 25, 15))