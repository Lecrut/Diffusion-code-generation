def max_temp_c_to_f(temps_c):
    max_c = max(temps_c)
    return (max_c * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [20, 25, 18, 30, 22]
    print(max_temp_c_to_f(sample_temps))