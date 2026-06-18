def reverse_string(s: str) -> str:
    return ''.join(reversed(s)) if isinstance(s, str) else s[::-1]

if __name__ == '__main__':
    print(reverse_string("Hello World"))  # Output: dlroW olleH