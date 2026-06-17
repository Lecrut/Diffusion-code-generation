import math
def sort_by_abs_magnitude(*temps):
    if not temps:
        return []
    n = len(temps)
    if n == 0:
        return []
    pairs = []
    for t in temps:
        abs_t = math.fabs(t)
        pairs.append((abs_t, float(t)))
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    return [t for _, t in sorted_pairs]
if __name__ == '__main__':
    sample_temps = 23.5, -10.2, 0.0, math.pi, -math.e, 42.789
    result = sort_by_abs_magnitude(*sample_temps)
    print(result)