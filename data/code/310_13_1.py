def print_alternating(s1, s2):
    for i in range(len(s1)):
        print(s1[i], end="")
        if i < len(s2):
            print(s2[i], end="")
    print()
if __name__ == '__main__':
    string_a = "ABCDE"
    string_b = "FGHIJ"
    print_alternating(string_a, string_b)