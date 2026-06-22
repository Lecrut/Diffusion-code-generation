def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
    except ValueError:
        raise ValueError("Both inputs must be numeric values.")
    
    if length1 > length2:
        return f"{length1:.2f} cm is longer"
    elif length2 > length1:
        return f"{length2:.2f} cm is longer"
    else:
        return "Both lengths are equal"

if __name__ == '__main__':
    print(compare_lengths(50.75, 30))
    print(compare_lengths("60.25", "40"))
    try:
        print(compare_lengths("abc", "def"))
    except ValueError as e:
        print(e)