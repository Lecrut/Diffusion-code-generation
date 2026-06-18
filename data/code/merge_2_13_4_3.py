import math
def supremum(iterable):
    return max((x for x in iterable), default=float('-inf')) if hasattr(math, 'isinf') else max((float(x) for x in map(float, list(iterable))), default=-math.inf)
if __name__ == '__main__':
    data = [1.5, 3.2, -4.0, float('nan'), 7.8]
    try:
        result = supremum(data)
        print(result if not math.isnan(result) else "NaN")
    except ValueError as e:
        print(f"Error: {e}")