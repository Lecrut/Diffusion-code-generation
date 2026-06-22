import re

def split_preserving_quotes(text):
    if not text:
        return []
    pattern = r"""
        (
            "[^"]*" |      # Match double-quoted strings
            '[^']*' |      # Match single-quoted strings
            [^,]+          # Match any sequence of non-comma characters
        )
    """
    matches = re.findall(pattern, text, re.VERBOSE)
    tokens = []
    for match in matches:
        cleaned = match.strip()
        if cleaned.startswith('"') and cleaned.endswith('"'):
            tokens.append(cleaned[1:-1])
        elif cleaned.startswith("'") and cleaned.endswith("'"):
            tokens.append(cleaned[1:-1])
        else:
            if cleaned:
                tokens.append(cleaned)
    return tokens

if __name__ == '__main__':
    sample_input = 'apple, "banana, split", cherry, "date", fig'
    result = split_preserving_quotes(sample_input)
    print(result)