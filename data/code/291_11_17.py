def compare_lengths(length1, length2):
    try:
        length1 = float(length1)
        length2 = float(length2)
        if length1 > length2:
            return f"{length1:.2f} cm is longer"
        elif length2 > length1:
            return f"{length2:.2f} cm is longer"
        else:
            return "Both measurements are equal"
    except ValueError:
        return "Invalid input. Please enter numeric values for the lengths."

if __name__ == '__main__':
    print(compare_lengths(150, 200))
    print(compare_lengths("300", "250"))
    print(compare_lengths("abc", "def"))