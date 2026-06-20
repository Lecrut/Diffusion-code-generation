def analyze_lengths(a, b):
    difference = abs(a - b)
    larger = max(a, b)
    smaller = min(a, b)
    if smaller == 0:
        ratio = float('inf') if larger != 0 else 0
    else:
        ratio = larger / smaller
    return {
        'length_a': a,
        'length_b': b,
        'difference': difference,
        'ratio': ratio
    }

if __name__ == '__main__':
    print(analyze_lengths(10, 5))