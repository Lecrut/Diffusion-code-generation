def is_temperature_safe(temp):
    return 15 <= temp <= 30

if __name__ == '__main__':
    sample_temp = 25
    if not isinstance(sample_temp, (int, float)):
        print("Error: Invalid temperature input")
    else:
        result = is_temperature_safe(sample_temp)
        print(result)