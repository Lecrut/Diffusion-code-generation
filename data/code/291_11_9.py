def compare_measurements(a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Error: Both inputs must be numeric."
    
    if a > b:
        return f"{a:.2f} cm"
    elif b > a:
        return f"{b:.2f} cm"
    else:
        return "Measurements are equal."

if __name__ == '__main__':
    print(compare_measurements(150.75, 149.25))