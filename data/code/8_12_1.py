import re

def split_quoted_string(s: str) -> list[str]:
    pattern = r'(?:^|,)\s*"([^"]*)"|[^,]+'
    matches = re.finditer(pattern, s)
    result = []
    for match in matches:
        token = match.group(0).strip()
        if not token:
            continue
        if token.startswith('"') and token.endswith('"'):
            token = token[1:-1]
        result.append(token)
    return result

if __name__ == '__main__':
    sample_input = 'John, "Alice, Bob", 42, "Charlie" , "Eve, "Frank""'
    tokens = split_quoted_string(sample_input)
    print(tokens)