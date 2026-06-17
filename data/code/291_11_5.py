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
    print(compare_lengths(list_a, list_b))
    string_x = "hello"
    string_y = "world"
    print(compare_lengths(string_x, string_y))
    string_z = "abc"
    string_w = "xyz"
    print(compare_lengths(string_z, string_w))
    list_c = [10]
    list_d = [20]
    print(compare_lengths(list_c, list_d))