def has_repeated_letters(s):
    return len(s) != len(set(s))
if __name__ == '__main__':
    string1 = "hello"
    string2 = "world"
    string3 = "programming"
    string4 = "abcde"
    print(f"'{string1}' has repeated letters: {has_repeated_letters(string1)}")
    print(f"'{string2}' has repeated letters: {has_repeated_letters(string2)}")
    print(f"'{string3}' has repeated letters: {has_repeated_letters(string3)}")
    print(f"'{string4}' has repeated letters: {has_repeated_letters(string4)}")