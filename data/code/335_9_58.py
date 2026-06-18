import sys
def main():
    text = "Hello world! This is a test string."
    words = text.split()
    result_list = [word.lower().strip("!,.") for word in words]
    print(f"Original: {text}")
    print(f"Split list length: {len(words)}")
    print(f"Purified list: {result_list}")
if __name__ == '__main__':
    main()