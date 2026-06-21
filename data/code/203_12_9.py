def compare_strings(str1, str2):
    if len(str1) > len(str2):
        return (str1, "greater")
    elif len(str1) < len(str2):
        return (str2, "greater")
    else:
        if str1 > str2:
            return (str1, "greater")
        elif str1 < str2:
            return (str2, "greater")
        else:
            return ("equal", "equal")

if __name__ == '__main__':
    print(compare_strings("apple", "banana"))
    print(compare_strings("cherry", "berry"))
    print(compare_strings("date", "date"))