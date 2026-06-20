def is_safe_temperature(temp):
    return 15 <= temp <= 30

if __name__ == '__main__':
    sample_temperatures = [12, 25, 35, 18]
    results = [is_safe_temperature(t) for t in sample_temperatures]
    print(results)