def compare_lengths(length1_cm, length2_cm):
    if length1_cm < length2_cm:
        return f"{length1_cm} cm"
    else:
        return f"{length2_cm} cm"

if __name__ == '__main__':
    print(compare_lengths(150, 200))