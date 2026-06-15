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
def extract_nested_pairs(s):
    pairs = []
    stack = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                start_index = stack.pop()
                end_index = i
                pairs.append((start_index, end_index))
    return pairs
if __name__ == '__main__':
    test_string1 = "a(b(c)d)e"
    test_string2 = "(a(b)c)(d(e))"
    test_string3 = "((x)y)z"
    test_string4 = "abc"
    test_string5 = "()(())"
    print(f"Test 1: {extract_nested_pairs(test_string1)}")
    print(f"Test 2: {extract_nested_pairs(test_string2)}")
    print(f"Test 3: {extract_nested_pairs(test_string3)}")
    print(f"Test 4: {extract_nested_pairs(test_string4)}")
    print(f"Test 5: {extract_nested_pairs(test_string5)}")