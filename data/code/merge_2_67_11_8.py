def sort_by_absolute_magnitude(*temps):
    if not temps:
        return []
    converted = [float(t) for t in temps]
    converted.sort(key=lambda x: abs(x))
    return converted
if __name__ == '__main__':
    sample_temps = [-10.5, 3.2, -7.89, 0, 44.1]
    result = sort_by_absolute_magnitude(*sample_temps)
    print(result)