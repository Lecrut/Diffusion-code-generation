def trim_string(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    sample_text = "   Python is elegant   "
    print(trim_string(sample_text))
    print(trim_string("  no leading or trailing  "))
    print(trim_string("\t\n\t\t  mixed whitespace  \t\n\t"))