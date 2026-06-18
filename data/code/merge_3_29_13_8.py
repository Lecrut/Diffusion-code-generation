import sys

def reverse_string(s):
    """Reverses a string efficiently using slice notation."""
    return s[::-1]

if __name__ == '__main__':
    test_cases = ["hello", "Python 3.9", "!dlroW olleh"]
    for case in test_cases:
        print(f"Original: {case} -> Reversed: {reverse_string(case)}")