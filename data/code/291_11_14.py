def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
    except ValueError:
        return "Invalid input. Please enter numeric values."
    
    if length1 > length2:
        return f"{length1:.2f} cm"
    elif length2 > length1:
        return f"{length2:.2f} cm"
    else:
        return "Both lengths are equal."

if __name__ == '__main__':
    print(compare_lengths(150.75, 200.34))