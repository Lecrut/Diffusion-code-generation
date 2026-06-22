def avg_temp_c_to_f(temps):
    avg_c = sum(temps) / len(temps)
    return (avg_c * 9/5) + 32

if __name__ == '__main__':
    sample_temps = [10, 20, 30, 40, 50]
    print(avg_temp_c_to_f(sample_temps))