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
            return ("equal", "in both metrics")

if __name__ == '__main__':
    result = compare_strings("apple", "banana")
    print(result)