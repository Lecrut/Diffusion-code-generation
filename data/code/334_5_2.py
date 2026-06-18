def combined_generator(str1: str, str2: str):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings.")
    i = 0
    j = 0
    while True:
        char1 = None
        char2 = None
        try:
            if i < len(str1):
                char1 = str1[i]
                i += 1
            if j < len(str2):
                char2 = str2[j]
                j += 1
        except IndexError:
            pass
        result_char = None
        if i < len(str1) and (not char2 or char1 != ''):
            result_char = str1[i]
        elif j < len(str2):
            result_char = str2[j]
        else:
            break
        yield result_char
if __name__ == '__main__':
    s_a = "Hello"
    s_b = "World!"
    for char in combined_generator(s_a, s_b):
        print(char)