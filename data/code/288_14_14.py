def is_temperature_in_range(temp, min_temp, max_temp):
    if not (isinstance(temp, (int, float)) and isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float))):
        return False
    if min_temp > max_temp:
        raise ValueError("Invalid range specified.")
    return min_temp <= temp <= max_temp

if __name__ == '__main__':
    sample_temp = 22.5
    sample_min_temp = 20
    sample_max_temp = 30
    print(is_temperature_in_range(sample_temp, sample_min_temp, sample_max_temp))