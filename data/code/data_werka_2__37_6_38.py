def interleave_strings(str1, str2):
    result = []
    for char1, char2 in zip(str1, str2):
        result.append(char1)
        result.append(char2)
    result.append(str1[len(str2):])
    result.append(str2[len(str1):])
    return ''.join(result)

if __name__ == '__main__':
    string1 = "abc"
    string2 = "12345"
    combined_string = interleave_strings(string1, string2)
    print(combined_string)