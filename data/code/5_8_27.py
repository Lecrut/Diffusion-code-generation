def compare_lengths(length1, length2):
    abs_diff = abs(length1 - length2)
    if length1 > length2:
        description = f"{length1} is greater than {length2}"
    elif length2 > length1:
        description = f"{length2} is greater than {length1}"
    else:
        description = "Both lengths are equal"
    
    return (abs_diff, description)

if __name__ == '__main__':
    length1 = 5.7
    length2 = 3.2
    result = compare_lengths(length1, length2)
    print(result)