def remove_spaces(s: str) -> str: return ''.join(c for c in s if ' ' != c)

if __name__ == '__main__': print(remove_spaces("Hello World"))