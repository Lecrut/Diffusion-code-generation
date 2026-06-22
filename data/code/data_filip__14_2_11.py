def all_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdef"
    result = all_unique(test_string)
    print(result)