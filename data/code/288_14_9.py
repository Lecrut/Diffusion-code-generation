def is_temperature_in_range(temp, min_temp, max_temp):
    if not (isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float))):
        return False
    if min_temp > max_temp:
        return False
    return min_temp <= temp <= max_temp
if __name__ == '__main__':
    print(is_temperature_in_range(25, 20, 30))
    print(is_temperature_in_range(15, 20, 30))
    print(is_temperature_in_range(25, 'a', 30))
    print(is_temperature_in_range(25, 30, 20))