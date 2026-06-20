def capitalize_first_alnum(s):
    result = []
    for char in s:
        if char.isalnum():
            result.append(char.upper())
            break
        result.append(char)
    result.extend(list(s[len(result):]))
    return "".join(result)

if __name__ == '__main__':
    print(capitalize_first_alnum("  hello"))
    print(capitalize_first_alnum("123abc"))
    print(capitalize_first_alnum("!!world"))
    print(capitalize_first_alnum("a"))