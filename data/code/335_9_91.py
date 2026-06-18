text = "Hello world! This is a test string."
words = text.split()
print(f"Total words: {len(words)}")
for word in reversed(words):
    print(word)
if __name__ == '__main__':
    pass