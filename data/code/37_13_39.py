def merge_strings(str1, str2):
    return ''.join([str1[i] + str2[i] for i in range(len(str1))])

if __name__ == '__main__':
    string1 = "abc"
    string2 = "123"
    result = merge_strings(string1, string2)
    print(result)