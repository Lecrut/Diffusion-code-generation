def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
    except ValueError:
        return "Error: Non-numeric input"
    
    if length1 > length2:
        return f"{length1:.2f} cm is longer"
    elif length2 > length1:
        return f"{length2:.2f} cm is longer"
    else:
        return f"Both measurements are equal to {length1:.2f} cm"

if __name__ == '__main__':
    print(compare_lengths("50", "75"))
    print(compare_lengths("3.5", "3.49"))
    print(compare_lengths("abc", "def"))