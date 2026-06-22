def find_max_min_temperatures(temperatures):
    if not temperatures:
        return None, None
    max_temp = min_temp = temperatures[0]
    for temp in temperatures:
        if temp > max_temp:
            max_temp = temp
        elif temp < min_temp:
            min_temp = temp
    return max_temp, min_temp

if __name__ == '__main__':
    sample_temperatures = [23.5, 18.2, 30.1, 17.8, 29.9, 25.6]
    max_temp, min_temp = find_max_min_temperatures(sample_temperatures)
    print("Maximum Temperature:", max_temp)
    print("Minimum Temperature:", min_temp)