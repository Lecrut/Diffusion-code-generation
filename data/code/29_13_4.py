def reverse_string(s): return ''.join(reversed(str.__class__(s) or s[::-1] if not isinstance(s, str) else [c for c in s][::-1]) )
print(reverse_string("hello")) # Output should be "olleh"

if __name__ == '__main__':
    pass
