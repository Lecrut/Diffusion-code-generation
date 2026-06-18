def sort_temperatures(*temps):
    if not temps:
        return []
    result = [float(t) for t in temps]
    result.sort(key=abs)
    return result
if __name__ == '__main__':
    sample_values = [-45.2, 10.5, -3.7, 0.0, 98.6]
    output = sort_temperatures(*sample_values)
    print(output)