def capitalize_first(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    result1 = capitalize_first("hello")
    print(result1)
    result2 = capitalize_first("world")
    print(result2)
    result3 = capitalize_first("a")
    print(result3)
    result4 = capitalize_first("")
    print(result4)
    result5 = capitalize_first("1abc")
    print(result5)