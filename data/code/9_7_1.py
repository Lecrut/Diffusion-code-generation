import string

def normalize_text(data: str) -> str:
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    stripped = data.strip()
    normalized = stripped.lower()
    cleaned = string.punctuation.replace('-', '')
    for char in cleaned:
        normalized = normalized.replace(char, '')
    words = normalized.split()
    result = ' '.join(words)
    return result

def main() -> None:
    sample_input = "  Hello, World!  This is a   TEST.  "
    result = normalize_text(sample_input)
    print(result)

if __name__ == '__main__':
    main()