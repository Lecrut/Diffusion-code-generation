def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

if __name__ == '__main__':
    samples = ["Hello World", "  Leading spaces   ", "", "NoSpacesHere"]
    for sample in samples:
        print(f"Input: {sample!r} => Output: {remove_spaces(sample)!r}")