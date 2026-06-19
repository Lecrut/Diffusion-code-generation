class StringReverser:
    def reverse(self, text):
        return text[::-1]

if __name__ == '__main__':
    reverser = StringReverser()
    sample_values = ["Hello, World!", "Python is great.", "!dlroW ,olleH", "", "a!b@c#d$"]
    for value in sample_values:
        print(f"Original: {value} -> Reversed: {reverser.reverse(value)}")