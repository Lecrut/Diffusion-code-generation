def is_balanced(expression):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            continue
    
    return not stack

if __name__ == '__main__':
    sample_expression = "({[]})"
    print(is_balanced(sample_expression))