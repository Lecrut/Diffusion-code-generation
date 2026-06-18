def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == '__main__':
    samples = ["hello", "Python 3.9"]
    print(f"Reversed 'hello': {reverse_string(samples[0])}")
    print(f"Reversed 'Python 3.9': {reverse_string(samples[1])}")