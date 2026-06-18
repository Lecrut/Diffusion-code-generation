from __future__ import annotations

def reverse_string(s: str) -> str:
    """Reverse a given string efficiently using slicing."""
    return s[::-1]

if __name__ == "__main__":
    samples = ["hello", "world!", "Python is great"]
    for sample in samples:
        print(f"Original: {sample}, Reversed: {reverse_string(sample)}")