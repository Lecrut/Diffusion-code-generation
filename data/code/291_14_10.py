def compare_string_lengths(str1, str2):
    if len(str1) > len(str2):
        return f"'{str1}' is longer than '{str2}'"
    elif len(str1) < len(str2):
        return f"'{str2}' is longer than '{str1}'"
    else:
        return "Both strings are of equal length"

if __name__ == '__main__':
    print(compare_string_lengths("hello", "world"))
    print(compare_string_lengths("short", "longer string"))
    print(compare_string_lengths("equal", "equal"))