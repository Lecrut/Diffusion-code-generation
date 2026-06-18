def reverse_string(s: str) -> str:
    return ''.join(reversed(s)) if s else ""

if __name__ == '__main__':
    sample_input = "Hello, World!"
    result = reverse_string(sample_input)
    print(f"Original: {sample_input}")
    print(f"Reversed: {result}")