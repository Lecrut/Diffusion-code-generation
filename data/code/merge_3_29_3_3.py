def reverse_string(s):
    return s[::-1]

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "Python", "!olleH"]
    results = [reverse_string(s) for s in sample_strings]
    print("Input\tReverse")
    for i, (inp, rev) in enumerate(zip(sample_strings, results)):
        print(f"{inp}\t{rev}")