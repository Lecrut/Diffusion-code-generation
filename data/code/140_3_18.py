def is_temperature_safe(temp):
    return 15 <= temp <= 30

if __name__ == '__main__':
    sample_temp = 25
    print(is_temperature_safe(sample_temp))