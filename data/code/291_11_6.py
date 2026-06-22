def compare_measurements(a, b):
    try:
        a = float(a)
        b = float(b)
        return max(a, b)
    except ValueError:
        return "Invalid input"

if __name__ == '__main__':
    print(compare_measurements(150.75, 200.34))