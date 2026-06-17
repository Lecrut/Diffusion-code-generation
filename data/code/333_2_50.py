import sys
def main():
    sentence = "Hello world this is a test"
    words = sentence.split()
    for word in words:
        print(word[0])
if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as f:
            input_data = f.read().strip()
        if not input_data:
            sys.exit(1)
        words = input_data.split()
        for word in words:
            print(word[0])
    except FileNotFoundError:
        sentence = "Hello world this is a test"
        words = sentence.split()
        for word in words:
            print(word[0])
    except Exception as e:
        sys.exit(1)