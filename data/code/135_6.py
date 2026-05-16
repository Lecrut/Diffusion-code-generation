def parse_logic(code):
    tokens = []
    current_level = 0
    for char in code:
        if char in ('if', 'elif', 'else'):
            tokens.append(char)
        elif char in ('(', ')'):
            tokens.append(char)
        elif char.isalpha() or char.isdigit():
            tokens.append(char)
        elif char in (' ', '\t'):
            continue
        else:
            tokens.append(char)
    return tokens
def normalize_structure(code):
    tokens = parse_logic(code)
    if not tokens:
        return tuple()
    structure = []
    stack = []
    token_index = 0
    while token_index < len(tokens):
        token = tokens[token_index]
        if token == 'if':
            condition_start = token_index + 1
            condition_tokens = []
            while token_index < len(tokens) and tokens[token_index] not in ('elif', 'else', ':'):
                condition_tokens.append(tokens[token_index])
                token_index += 1
            if not condition_tokens:
                continue
            condition_str = " ".join(condition_tokens)
            structure.append(('if', condition_str))
            while token_index < len(tokens) and tokens[token_index] != 'else' and tokens[token_index] != ':':
                if tokens[token_index] == 'elif':
                    token_index += 1
                    condition_tokens = []
                    while token_index < len(tokens) and tokens[token_index] not in ('else', ':'):
                        condition_tokens.append(tokens[token_index])
                        token_index += 1
                    if condition_tokens:
                        structure.append(('elif', " ".join(condition_tokens)))
                else:
                    break
            if token_index < len(tokens) and tokens[token_index] == 'else':
                structure.append(('else', None))
                token_index += 1
        token_index += 1
    return tuple(structure)
def compare_equivalence(code1, code2):
    structure1 = normalize_structure(code1)
    structure2 = normalize_structure(code2)
    if len(structure1) != len(structure2):
        return False
    for item1, item2 in zip(structure1, structure2):
        if item1 != item2:
            return False
    return True
if __name__ == '__main__':
    code_a = "if x > 5: print('A')"
    code_b = "if x > 5: print('A')"
    code_c = "if x > 5: print('B')"
    code_d = "if x > 5: print('A')"
    print(f"Comparing A and B: {compare_equivalence(code_a, code_b)}")
    print(f"Comparing A and C: {compare_equivalence(code_a, code_c)}")
    print(f"Comparing A and D: {compare_equivalence(code_a, code_d)}")
    code_e = "if x > 5: print('A')"
    code_f = "if x > 5: print('A')"
    print(f"Comparing E and F: {compare_equivalence(code_e, code_f)}")
    code_g = "if x > 5: print('A')"
    code_h = "if x > 6: print('A')"
    print(f"Comparing G and H: {compare_equivalence(code_g, code_h)}")