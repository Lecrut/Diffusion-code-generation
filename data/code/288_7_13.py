def max_temp_c_to_f(temps):
    max_c = max(temps)
    return (max_c * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [20, 25, 15, 30, 28]
    print(max_temp_c_to_f(sample_temps))