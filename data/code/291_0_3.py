def compare_string_lengths():
    string1 = "hello"
    string2 = "world"
    length1 = len(string1)
    length2 = len(string2)
    if length1 > length2:
        print(f"The length of '{string1}' ({length1}) is greater than the length of '{string2}' ({length2}).")
    elif length1 < length2:
        print(f"The length of '{string1}' ({length1}) is less than the length of '{string2}' ({length2}).")
    else:
        print(f"The length of '{string1}' ({length1}) is equal to the length of '{string2}' ({length2}).")
if __name__ == '__main__':
    compare_string_lengths()