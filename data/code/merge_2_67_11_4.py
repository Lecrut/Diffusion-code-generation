def sort_temperatures(*temps):
    if not temps:
        return []
    abs_vals = [(t, t) for t in temps]
    sorted_abs = sorted(abs_vals, key=lambda x: -abs(x[0]))
    result = [x[1] for x in sorted_abs]
    return result
if __name__ == '__main__':
    sample_temps = [-5.2, 3.7, -8.9, 0.0, 4.1, -2.3]
    print(sort_temperatures(*sample_temps))