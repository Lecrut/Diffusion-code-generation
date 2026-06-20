def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    samples = ['  hello  ', '\t\nworld\n\t', '   no   spaces   ', '', '   ']
    for sample in samples:
        print(strip_whitespace(sample))