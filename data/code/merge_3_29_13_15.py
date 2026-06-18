reversed_str = lambda s: "".join(reversed(s)) if isinstance(s, str) else "Not a string"
if __name__ == '__main__':
    print(reversed_str("Hello"))  # Output: olleH
    print(reversed_str(12345))   # Output: Not a string