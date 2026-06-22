CHAR_COUNT_DICT = {}

def count_characters(s):
    char_count_dict = CHAR_COUNT_DICT.copy()
    for char in s:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

if __name__ == '__main__':
    sample_string = "Python programming is fun!"
    result = count_characters(sample_string)
    print(result)