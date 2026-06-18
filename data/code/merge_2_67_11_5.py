def sort_temperatures(temps):
    for i in range(len(temps)):
        min_idx = i
        abs_val_i = abs(temps[i])
        for j in range(i + 1, len(temps)):
            if abs(temps[j]) < abs_val_i:
                temp_j = temps[min_idx]
                temps[min_idx] = temps[j]
                temps[j] = temp_j
                min_idx = j
    return temps
if __name__ == '__main__':
    sample_temps = [3.5, -10.2, 4.8, -7.9, 2.1]
    result = sort_temperatures(sample_temps)
    print(result)