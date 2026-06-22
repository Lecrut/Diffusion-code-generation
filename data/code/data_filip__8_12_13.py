import re

def split_quoted_commas(text: str) -> list:
    pattern = re.compile(r'(".*?"|\'[^\']*\'|[^,]+)')
    tokens = [m.group(1).strip() for m in pattern.finditer(text)]
    result = []
    for token in tokens:
        if not token:
            continue
        if (token.startswith('"') and token.endswith('"')) or (token.startswith("'") and token.endswith("'")):
            token = token[1:-1]
        result.append(token)
    return result

if __name__ == '__main__':
    sample_input = 'name, "john doe", 25, "hello, world", age'
    output = split_quoted_commas(sample_input)
    print(output)