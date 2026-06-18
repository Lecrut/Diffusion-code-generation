import sys
def main():
    text = "Hello world! This is a Pythonic example."
    words_list = text.split()
    print("Words found:", len(words_list))
    for word in words_list:
        if not any(char.isdigit() or char == '!' or char == '.' for char in word):
            print(word)
if __name__ == '__main__':
    sys.exit(0)