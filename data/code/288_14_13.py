TEMPERATURE_MIN = -273.15

def is_temperature_in_range(temp, min_temp, max_temp):
    if not all((isinstance(i, (int, float)) for i in [temp, min_temp, max_temp])):
        return False
    if min_temp > max_temp or min_temp < TEMPERATURE_MIN:
        return False
    return min_temp <= temp <= max_temp
if __name__ == '__main__':
    print(is_temperature_in_range(20, 15, 25))
    print(is_temperature_in_range(30, 20, 25))
    print(is_temperature_in_range('a', 15, 25))
    print(is_temperature_in_range(20, 25, 15))