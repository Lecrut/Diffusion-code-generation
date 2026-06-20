TEMP_MIN = 15
TEMP_MAX = 30

is_within_range = lambda temp: TEMP_MIN <= temp <= TEMP_MAX

if __name__ == '__main__':
    sample_temps = [20, 14, 31]
    results = list(map(is_within_range, sample_temps))
    print(results)