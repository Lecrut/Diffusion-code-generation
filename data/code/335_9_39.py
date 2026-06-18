import sys
def main():
    text = "Hello world! This is a test."
    words = [word.strip() for word in text.split()]
    if len(words) > 0:
        print(f"First word: {words[0]}")
        last_word = words[-1]
        print(f"Last word: {last_word}")
if __name__ == '__main__':
    sys.exit(0)