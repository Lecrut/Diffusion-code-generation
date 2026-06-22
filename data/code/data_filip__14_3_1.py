def is_unique_chars(s):
    if not s:
        return True
    char_list = list(s)
    n = len(char_list)
    for i in range(n):
        for j in range(i + 1, n):
            if char_list[i] > char_list[j]:
                temp = char_list[i]
                char_list[i] = char_list[j]
                char_list[j] = temp
    for k in range(n - 1):
        if char_list[k] == char_list[k + 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "programming"
    result = is_unique_chars(sample_string)
    print(result)