def reverse_string(s):
    if not s:
        return ""
    return s[::-1]

class Reverser:
    def __init__(self, text):
        self.text = text
    def get_reversed(self):
        return reverse_string(self.text)

if __name__ == '__main__':
    sample_string = "Hello, 世界!"
    reverser = Reverser(sample_string)
    reversed_string = reverser.get_reversed()
    print(reversed_string)