def capitalize_strings(string_tuple):
    return tuple(s.capitalize() for s in string_tuple)

if __name__ == '__main__':
    result = capitalize_strings(("hello", "WORLd", "PyThOn"))
    print(result)