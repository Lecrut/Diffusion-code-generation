def compare_lengths(length1, length2):
    if length1 > length2:
        greater_name = "length1"
        is_length1_greater = True
    elif length2 > length1:
        greater_name = "length2"
        is_length1_greater = False
    else:
        greater_name = "equal"
        is_length1_greater = False
    return {
        "length1": length1,
        "length2": length2,
        "greater": greater_name,
        "is_length1_greater": is_length1_greater
    }

if __name__ == '__main__':
    result = compare_lengths(10, 5)
    print(result)