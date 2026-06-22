def compare_string_lengths(str1, str2):
    if len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2
    else:
        return "Equal"

if __name__ == '__main__':
    result = compare_string_lengths("hello", "world")
    print(result)