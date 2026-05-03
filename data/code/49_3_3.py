if __name__ == '__main__':
    length1_str = "15.7"
    length2_str = "22.3"
    length1 = float(length1_str)
    length2 = float(length2_str)
    if length1 > length2:
        print(f"{length1} is longer than {length2}")
    elif length2 > length1:
        print(f"{length2} is longer than {length1}")
    else:
        print(f"{length1} and {length2} are equal in length")