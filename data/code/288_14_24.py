def is_temperature_in_range(temp, min_temp, max_temp):
    conversions = {'C': lambda t: t, 'F': lambda t: (t - 32) * 5 / 9, 'K': lambda t: t - 273.15}
    if not isinstance(temp, (int, float)) or not all((isinstance(i, (int, float)) for i in [min_temp, max_temp])):
        return False
    scale = temp
    min_temp_c = conversions[scale](min_temp)
    max_temp_c = conversions[scale](max_temp)
    temp_c = conversions[scale](temp)
    return min_temp_c <= temp_c <= max_temp_c
if __name__ == '__main__':
    print(is_temperature_in_range(20, 15, 25))
    print(is_temperature_in_range(30, 20, 25))
    print(is_temperature_in_range('a', 15, 25))
    print(is_temperature_in_range(20, 25, 15))
    print(is_temperature_in_range(68, 60, 70))
    print(is_temperature_in_range(-40, -100, 0))