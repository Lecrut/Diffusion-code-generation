def trim(s): return s.strip()
if __name__ == '__main__':
    samples = ["  hello  ", "\tworld\n", "   ", "no_change"]
    for sample in samples:
        print(trim(sample))