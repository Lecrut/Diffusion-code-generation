def contains_repeated_letters(s):
    return len(s) != len(set(s))
if __name__ == '__main__':
    string1 = "hello"
    string2 = "world"
    string3 = "abcde"
    string4 = "programming"
    print(f"'{string1}': {contains_repeated_letters(string1)}")
    print(f"'{string2}': {contains_repeated_letters(string2)}")
    print(f"'{string3}': {contains_repeated_letters(string3)}")
    print(f"'{string4}': {contains_repeated_letters(string4)}")