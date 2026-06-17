def capitalize_string(input_string):
    if not input_string:
        return ""
    return input_string.upper()
if __name__ == '__main__':
    print(capitalize_string(""))
    print(capitalize_string("hello"))
    print(capitalize_string("WORLD"))
    print(capitalize_string("MiXeD CaSe"))