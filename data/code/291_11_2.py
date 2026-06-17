def compare_lengths(seq1, seq2):
    if len(seq1) > len(seq2):
        return (seq1, "longer")
    elif len(seq2) > len(seq1):
        return (seq2, "longer")
    else:
        return (seq1, "equal")
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7]
    print(compare_lengths(list1, list2))
    string1 = "hello"
    string2 = "world"
    print(compare_lengths(string1, string2))
    list3 = [10, 20]
    list4 = [5, 6, 7]
    print(compare_lengths(list3, list4))
    string3 = "abc"
    string4 = "abc"
    print(compare_lengths(string3, string4))