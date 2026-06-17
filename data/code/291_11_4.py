def compare_lengths(seq1, seq2):
    if len(seq1) > len(seq2):
        return (seq1, "longer")
    elif len(seq2) > len(seq1):
        return (seq2, "longer")
    else:
        return (seq1, "equal")
if __name__ == '__main__':
    list_a = [1, 2, 3, 4, 5]
    list_b = [6, 7]
    result1 = compare_lengths(list_a, list_b)
    print(f"Comparing {list_a} and {list_b}: {result1}")
    string_x = "hello"
    string_y = "world"
    result2 = compare_lengths(string_x, string_y)
    print(f"Comparing '{string_x}' and '{string_y}': {result2}")
    list_c = [10, 20]
    list_d = [30, 40]
    result3 = compare_lengths(list_c, list_d)
    print(f"Comparing {list_c} and {list_d}: {result3}")
    list_e = [1, 2, 3]
    list_f = [1, 2, 3]
    result4 = compare_lengths(list_e, list_f)
    print(f"Comparing {list_e} and {list_f}: {result4}")