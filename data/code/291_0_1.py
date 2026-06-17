def compare_string_lengths():
    string1 = "hello"
    string2 = "world"
    length1 = len(string1)
    length2 = len(string2)
    if length1 > length2:
        print(f"Length of '{string1}' ({length1}) is greater than the length of '{string2}' ({length2}).")
    elif length1 < length2:
        print(f"Length of '{string1}' ({length1}) is less than the length of '{string2}' ({length2}).")
    else:
        print(f"The lengths of '{string1}' ({length1}) and '{string2}' ({length2}) are equal.")
if __name__ == '__main__':
    compare_string_lengths()