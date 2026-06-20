def trim_string(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    return text.strip()

if __name__ == "__main__":
    sample_1 = "   hello world   "
    sample_2 = "\t\n  python code  \t\n"
    sample_3 = "no_whitespace"
    sample_4 = "   "
    print(trim_string(sample_1))
    print(trim_string(sample_2))
    print(trim_string(sample_3))
    print(repr(trim_string(sample_4)))