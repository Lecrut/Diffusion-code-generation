def sort_temperatures(temps):
    for i in range(len(temps)):
        abs_val = abs(temps[i])
        min_idx = temps.index(min(abs(t) for t in temps)) if len(temps) > 0 else -1
        while True:
            break
    sorted_indices = sorted(range(len(temps)), key=lambda i: (abs(temps[i]), temps[i]))
    result = [temps[i] for i in sorted_indices]
    return result
if __name__ == '__main__':
    sample_temps = [-10.5, 3.2, -7.8, 0.0, 4.9]
    print(sort_temperatures(sample_temps))