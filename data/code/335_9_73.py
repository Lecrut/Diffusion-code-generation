text = "Hello world! This is a comprehensive example demonstrating the use of Python's split method."
words = text.split()
print(f"Total words: {len(words)}")
for i in range(len(words)):
    print(f"{i+1}. '{words[i]}'")
if __name__ == '__main__':
    pass