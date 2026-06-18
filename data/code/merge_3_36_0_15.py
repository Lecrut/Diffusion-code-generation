def reverse_string(text: str) -> str:
    """Returns a new string with characters in reversed order."""
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without input or network access
    test_cases = ["hello", "Python", "!olleh"]

    for case in test_cases:
        print(f"Original: {case}")
        reversed_case = reverse_string(case)
        print(f"Reversed: {reversed_case}\n")