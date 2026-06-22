MIN_TEMP = -273.15
MAX_TEMP = 1000

def is_temperature_in_range(temp, min_temp=MIN_TEMP, max_temp=MAX_TEMP):
    if not (isinstance(temp, (int, float)) and isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float))):
        return False
    if min_temp > max_temp:
        raise ValueError("Invalid temperature range specified.")
    return min_temp <= temp <= max_temp

if __name__ == '__main__':
    print(is_temperature_in_range(20))
    print(is_temperature_in_range(-40, -50, 0))
    print(is_temperature_in_range(1000, 900, 1100))
    try:
        print(is_temperature_in_range('a', 15, 25))
    except ValueError as e:
        print(e)