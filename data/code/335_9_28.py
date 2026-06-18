def main():
    text = "Hello world! This is a test string."
    words = text.split()
    clean_words = [word for word in words] 
    print(f"Original: {text}")
    print(f"Split result: {clean_words}")
if __name__ == '__main__':
    main()