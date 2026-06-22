def is_temperature_in_range(temp, min_temp, max_temp):
    if not all(isinstance(x, (int, float)) for x in [temp, min_temp, max_temp]):
        return False
    if min_temp > max_temp:
        return False
    return min_temp <= temp <= max_temp

if __name__ == '__main__':
    sample_temp = 23.5
    sample_min_temp = 20.0
    sample_max_temp = 25.0
    
    result = is_temperature_in_range(sample_temp, sample_min_temp, sample_max_temp)
    print(result)