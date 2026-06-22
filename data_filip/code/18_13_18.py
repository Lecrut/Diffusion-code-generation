def run_length_encode(source):
    if not source:
        return ""
    return "".join(
        f"{count}{char}"
        for count, char in (
            (sum(1 for _ in group), char)
            for char, group in __import__("itertools").groupby(source)
        )
    )

def run_length_decode(encoded):
    if not encoded:
        return ""
    digits = []
    result_parts = []
    for char in encoded:
        if char.isdigit():
            digits.append(char)
        else:
            if digits:
                count = int("".join(digits))
                result_parts.append(char * count)
                digits = []
    return "".join(result_parts)

if __name__ == "__main__":
    samples = [
        "AAABBBCCC",
        "X",
        "AABBBCCCCDDDD",
        "ABC",
        "",
        "111222333"
    ]
    for sample in samples:
        encoded = run_length_encode(sample)
        decoded = run_length_decode(encoded)
        print(f"Original: {repr(sample)}")
        print(f"Encoded:  {repr(encoded)}")
        print(f"Decoded:  {repr(decoded)}")
        print(f"Match:    {sample == decoded}")
        print()