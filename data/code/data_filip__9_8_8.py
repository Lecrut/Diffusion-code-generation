def strip_whitespace(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_text = "   Python is elegant   "
    print(strip_whitespace(sample_text))