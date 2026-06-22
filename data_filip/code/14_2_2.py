def all_unique_characters(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdefg"
    print(all_unique_characters(test_string))
    test_string = "aabbcc"
    print(all_unique_characters(test_string))