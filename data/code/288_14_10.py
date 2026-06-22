def is_temperature_in_range(temp, min_temp, max_temp):
    if not (isinstance(temp, (int, float)) and isinstance(min_temp, (int, float)) and isinstance(max_temp, (int, float))):
        return False
    if min_temp > max_temp:
        raise ValueError("Invalid range specified")
    return min_temp <= temp <= max_temp

if __name__ == '__main__':
    test_cases = [
        (20, 15, 25),
        (30, 20, 25),
        ('a', 15, 25),
        (20, 25, 15)
    ]
    
    for temp, min_temp, max_temp in test_cases:
        try:
            result = is_temperature_in_range(temp, min_temp, max_temp)
            print(f"Temperature {temp} in range ({min_temp}, {max_temp}): {result}")
        except ValueError as e:
            print(e)