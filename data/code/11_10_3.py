def calculate_ratio(length1, length2):
    if length2 == 0:
        return "Error: Cannot divide by zero"
    else:
        return length1 / length2
if __name__ == '__main__':
    a = 10
    b = 5
    ratio1 = calculate_ratio(a, b)
    print(f"Ratio of {a} and {b}: {ratio1}")
    c = 20
    d = 0
    ratio2 = calculate_ratio(c, d)
    print(f"Ratio of {c} and {d}: {ratio2}")
    e = 15
    f = 3
    ratio3 = calculate_ratio(e, f)
    print(f"Ratio of {e} and {f}: {ratio3}")