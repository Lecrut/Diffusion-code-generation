def sort_by_abs_magnitude(*temps):
    if not temps:
        return []
    data = [(float(t), abs(float(t))) for t in temps]
    sorted_data = sorted(data, key=lambda x: x[1])
    return [x[0] for x in sorted_data]
if __name__ == '__main__':
    sample_temps = 23.5, -45.67, 0.0, -89.1, 12.34
    result = sort_by_abs_magnitude(*sample_temps)
    print(result)