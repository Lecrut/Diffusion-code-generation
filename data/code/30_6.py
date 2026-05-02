def swap_adjacent(s):
    l = list(s)
    for i in range(len(l) - 1):
        l[i], l[i+1] = l[i+1], l[i]
    return "".join(l)
if __name__ == '__main__':
    test_string = "abcde"
    result = swap_adjacent(test_string)
    print(result)