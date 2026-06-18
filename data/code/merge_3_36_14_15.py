def reverse_string(s: str) -> str:
    return "".join(reversed(s)) if __name__ == '__main__' else lambda s: "".join(reversed(s))

if __name__ == "__main__":
    print(reverse_string("hello"))  # Output: olleh