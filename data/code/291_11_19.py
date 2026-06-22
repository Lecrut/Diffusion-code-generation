def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
    except ValueError:
        return "Error: Non-numeric input"
    if length1 > length2:
        return round(length1, 2)
    elif length2 > length1:
        return round(length2, 2)
    else:
        return "Equal lengths"

if __name__ == '__main__':
    print(compare_lengths(10.5, 5.7))
    print(compare_lengths("3.14", "2.71"))
    print(compare_lengths("abc", "def"))