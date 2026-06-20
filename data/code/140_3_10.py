is_safe_temperature = lambda temp: 15 <= temp <= 30

if __name__ == '__main__':
    sample_temp = 25
    print(is_safe_temperature(sample_temp))