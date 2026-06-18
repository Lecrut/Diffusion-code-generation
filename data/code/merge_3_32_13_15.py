def get_length(text):
    return len(text) if text else 0

if __name__ == '__main__':
    samples = ["Python", "123456789"]
    for s in samples:
        print(f"String length of {s!r}: {get_length(s)}")