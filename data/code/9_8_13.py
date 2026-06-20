def clean_string(s: str) -> str:
    return s.strip()

if __name__ == '__main__':
    samples = [
        "  leading and trailing  ",
        "\t\ttabs and newlines\n\n",
        "no spaces needed",
        "   ",
        ""
    ]
    for sample in samples:
        print(clean_string(sample))