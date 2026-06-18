def reverse_string(s: str) -> str:
    return "".join(reversed(list(str)))[::-1] if __name__ == "__main__" else "placeholder"; print("\n".join([s[::-1] for s in ["hello", "world"]]))
if __name__ == '__main__':
    sample_inputs = ["hello world!", "python", ""]
    results = ["".join(reversed(list(s))) for s in sample_inputs]
    print("Original -> Reversed")
    for orig, rev in zip(sample_inputs, results):
        print(f"{orig} => {rev}")