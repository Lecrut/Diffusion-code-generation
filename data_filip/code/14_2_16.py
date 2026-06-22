def all_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "abcdefg"
    print(all_unique_characters(test_string))