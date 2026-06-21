def compare_strings(s1, s2):
    if len(s1) > len(s2):
        return (s1, "greater")
    elif len(s1) < len(s2):
        return (s2, "greater")
    else:
        if s1 > s2:
            return (s1, "greater")
        elif s1 < s2:
            return (s2, "greater")
        else:
            return ("equal", "equal")

if __name__ == '__main__':
    print(compare_strings("apple", "banana"))
    print(compare_strings("cherry", "apricot"))
    print(compare_strings("blueberry", "blueberry"))