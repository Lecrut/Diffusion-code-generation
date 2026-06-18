def extract_substrings(text: str) -> list[str]:
    """Extract all substrings from text that fall between specified start and end points."""
    return [text[i:j] for i, j in [(0, 1), (2, 4)] if i < len(text) <= j <= len(text)]

if __name__ == '__main__':
    target_string = "hello world"
    result = extract_substrings(target_string)
    print(result)