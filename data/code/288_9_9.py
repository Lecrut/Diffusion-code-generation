def min_temp_f_to_c(temps_f):
    return min(temp - 32 * 5 / 9 for temp in temps_f)

if __name__ == '__main__':
    sample_temps = [32, 212, 0, -40]
    print(min_temp_f_to_c(sample_temps))