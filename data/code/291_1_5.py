def compare_lengths(length1, length2):
    if length1 < length2:
        return f"{length1} cm"
    else:
        return f"{length2} cm"

if __name__ == '__main__':
    print(compare_lengths(150, 200))
    print(compare_lengths(300, 250))