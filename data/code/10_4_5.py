def find_min_max_temp(temperatures):
    if not temperatures:
        return None, None
    min_temp = temperatures[0]
    max_temp = temperatures[0]
    for temp in temperatures:
        if temp < min_temp:
            min_temp = temp
        if temp > max_temp:
            max_temp = temp
    return max_temp, min_temp
if __name__ == '__main__':
    sample_temps = [25.5, 18.0, 30.1, 15.5, 22.8, 28.9]
    max_t, min_t = find_min_max_temp(sample_temps)
    print(f"Maximum temperature: {max_t}")
    print(f"Minimum temperature: {min_t}")