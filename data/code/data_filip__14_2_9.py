def are_all_characters_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdefg"
    print(are_all_characters_unique(test_string))