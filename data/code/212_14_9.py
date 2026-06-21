def find_min_max(data):
    if not data:
        return None, None
    minimum = maximum = data[0]
    for x in data[1:]:
        if x < minimum:
            minimum = x
        elif x > maximum:
            maximum = x
    return minimum, maximum

if __name__ == '__main__':
    sample_list = [3.14, 1.618, 2.718, -0.5, 100.0, -50.2]
    minimum_val, maximum_val = find_min_max(sample_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")