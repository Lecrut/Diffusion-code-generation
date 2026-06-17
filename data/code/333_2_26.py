import sys
def main():
    sentence = "Hello world this is a test"
    words = sentence.split()
    result = [word[0] for word in words if len(word) > 0]
    print("".join(result))
if __name__ == '__main__':
    sys.exit(0)