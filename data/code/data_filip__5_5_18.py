def capitalize_first(s):
    if not s:
        return s
    return [s[0].upper()] + list(s[1:])

def join_chars(char_list):
    return ''.join(char_list)

if __name__ == '__main__':
    sample = "hello world"
    result = join_chars(capitalize_first(sample))
    print(result)