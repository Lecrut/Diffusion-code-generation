import sys

def check_positive(value: str) -> bool:
    """Check if a string represents a positive number."""
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network)
    samples = [
        "1",
        "-5",
        "0.5",
        "abc",
        "3.14",
        "",
        "+2",
        "0"
    ]

    for sample in samples:
        result = check_positive(sample)
        print(f"{sample!r} -> {result}")