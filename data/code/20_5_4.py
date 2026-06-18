from math import isclose; print("1.0 vs 2.3:", isclose(1.0, 2.3)); print("1.5 vs 1.4999999999:", isclose(1.5, 1.4999999999))

if __name__ == '__main__':
    from math import isclose; results = [isclose(float(a), float(b)) for a, b in [(1.0, 2.3), (1.5, 1.4999999999), (1e-7, -1e-8)]]; print(f"Comparisons: {results}")