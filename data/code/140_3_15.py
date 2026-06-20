is_safe_temp = lambda temp: 15 <= temp <= 30

if __name__ == '__main__':
    sample_temps = [20, 14, 31]
    results = [is_safe_temp(temp) for temp in sample_temps]
    print(results)