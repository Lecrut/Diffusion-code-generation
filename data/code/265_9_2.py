def extract_parentheses(s):
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                top = stack.pop()
                result.append((top, char))
        elif stack:
            result.append((stack[-1], char))
    return result
if __name__ == '__main__':
    test_string1 = "a(b(c)d)e"
    print(extract_parentheses(test_string1))
    test_string2 = "((a)(b))"
    print(extract_parentheses(test_string2))
    test_string3 = "abc(def)ghi(jkl)"
    print(extract_parentheses(test_string3))
    test_string4 = "(()())"
    print(extract_parentheses(test_string4))