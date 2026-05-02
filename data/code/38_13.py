def contains_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    string1 = "hello"
    string2 = "world"
    string3 = "abcde"
    string4 = "programming"
    print(f"'{string1}' has repeated letters: {contains_repeated_letters(string1)}")
    print(f"'{string2}' has repeated letters: {contains_repeated_letters(string2)}")
    print(f"'{string3}' has repeated letters: {contains_repeated_letters(string3)}")
    print(f"'{string4}' has repeated letters: {contains_repeated_letters(string4)}")