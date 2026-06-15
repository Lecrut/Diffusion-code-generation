import math
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    n = len(data)
    s = sum(data)
    p = 1
    for x in data:
        p *= x
    mean = s / n
    variance = sum([(x - mean) ** 2 for x in data]) / n
    print(f"Sum: {s}")
    print(f"Product: {p}")
    print(f"Variance: {variance}")