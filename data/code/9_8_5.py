def sanitize(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    raw_input_1 = "   Pythonic elegance   "
    raw_input_2 = "\t\n  data cleaning  \r\n"
    print(sanitize(raw_input_1))
    print(sanitize(raw_input_2))