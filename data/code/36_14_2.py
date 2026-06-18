def reverse_string(s): return ''.join(reversed(s)) if isinstance(s, str) else list(s)[::-1]

if __name__ == '__main__':
    result = reverse_string("Hello World")
    print(result)