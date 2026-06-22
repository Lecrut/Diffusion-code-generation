class StringReverser:
    def reverse(self, text):
        return ''.join(reversed(text))

if __name__ == '__main__':
    samples = {
        "hello": "olleh",
        "world": "dlrow",
        "Python": "nohtyP",
        "!@#": "#@!"
    }
    
    reverser = StringReverser()
    for original, expected in samples.items():
        result = reverser.reverse(original)
        print(f"Original: {original}, Reversed: {result}, Expected: {expected}")