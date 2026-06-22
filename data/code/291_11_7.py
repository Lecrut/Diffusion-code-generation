def compare_measurements(cm1, cm2):
    try:
        cm1 = float(cm1)
        cm2 = float(cm2)
    except ValueError:
        return "Error: Non-numeric input"
    
    if cm1 > cm2:
        return f"{cm1:.2f} cm is longer"
    elif cm2 > cm1:
        return f"{cm2:.2f} cm is longer"
    else:
        return "Both measurements are equal"

if __name__ == '__main__':
    print(compare_measurements(150.75, 149.80))