def sort_temperatures(*temps):
    if not temps:
        return []
    for t in range(len(temps)):
        abs_val = abs(temps[t])
        for i in range(t + 1, len(temps)):
            if abs(temps[i]) < abs_val:
                temp_i = temps[i]
                temps[t], temps[i] = temps[i], t
    return sorted(range(len(temps)), key=lambda i: abs(temps[i]))
def process_temperatures(*args):
    if not args:
        return []
    temp_list = [float(x) for x in args]
    sorted_indices = sorted(range(len(temp_list)), key=lambda i: abs(temp_list[i]))
    return [temp_list[i] for i in sorted_indices]
if __name__ == '__main__':
    sample_temps = 23.5, -10.2, 45.8, -67.9, 0.0
    result = process_temperatures(*sample_temps)
    print(result)