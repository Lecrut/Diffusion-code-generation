def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
    except ValueError:
        return "Error: Non-numeric input provided."
    
    if length1 > length2:
        return f"{length1:.2f} cm is longer"
    elif length2 > length1:
        return f"{length2:.2f} cm is longer"
    else:
        return f"Both measurements are equal at {length1:.2f} cm"

if __name__ == '__main__':
    measurement_a = "50.75"
    measurement_b = "60.25"
    print(compare_lengths(measurement_a, measurement_b))