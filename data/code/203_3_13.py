LEXICOGRAPHIC_ORDER = -1
EQUAL = 0
REVERSE_LEXICOGRAPHIC_ORDER = 1

def compare_strings(str1, str2):
    if str1 < str2:
        return LEXICOGRAPHIC_ORDER
    elif str1 > str2:
        return REVERSE_LEXICOGRAPHIC_ORDER
    else:
        return EQUAL

if __name__ == '__main__':
    result = compare_strings("apple", "banana")
    print(result)