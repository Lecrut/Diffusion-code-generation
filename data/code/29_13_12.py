def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "Python3.9"]
    results = [reverse_string(sample) for sample in samples]
    print("\n".join(results))