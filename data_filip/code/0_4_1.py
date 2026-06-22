def sanitize_and_convert(s):
    digits_only = ''.join(c for c in s if c.isdigit())
    if not digits_only:
        return 0.0
    return float(digits_only)

if __name__ == '__main__':
    print(sanitize_and_convert("a123b456c"))
    print(sanitize_and_convert("12.34abc"))
    print(sanitize_and_convert("no_digits_here"))
    print(sanitize_and_convert("007"))