def extract_parentheses(s):
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                top = stack.pop()
                result.append((top, char))
    return result
if __name__ == '__main__':
    test_string1 = "a(b(c)d)e"
    test_string2 = "(a(b)c)(d)"
    test_string3 = "((x))y"
    test_string4 = "abc"
    test_string5 = "()(())"
    print(f"'{test_string1}': {extract_parentheses(test_string1)}")
    print(f"'{test_string2}': {extract_parentheses(test_string2)}")
    print(f"'{test_string3}': {extract_parentheses(test_string3)}")
    print(f"'{test_string4}': {extract_parentheses(test_string4)}")
    print(f"'{test_string5}': {extract_parentheses(test_string5)}")