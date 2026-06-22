def min_temp_f_to_c(temps):
    return min(temp - 32 * 5 / 9 for temp in temps)

if __name__ == '__main__':
    sample_temps = [32, 212, 0, -40]
    print(min_temp_f_to_c(sample_temps))