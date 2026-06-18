def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "Python 3.9"]
    results = [reverse_string(sample) for sample in samples]
    print("Input | Output")
    print("-" * 40)
    for inp, out in zip(samples, results):
        print(f"{inp} | {out}")