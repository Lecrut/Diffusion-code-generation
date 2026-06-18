def sort_temperatures(*temps):
    if not temps:
        return []
    result = [abs(t) for t in temps]
    sorted_indices = sorted(range(len(result)), key=lambda i: result[i])
    sorted_magnitudes = [result[i] for i in sorted_indices]
    return sorted_magnitudes
if __name__ == '__main__':
    sample_temps = [-10.5, 3.2, -7.89, 0, 42.1]
    output = sort_temperatures(*sample_temps)
    print(output)