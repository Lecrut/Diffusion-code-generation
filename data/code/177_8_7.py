def split_text(text):
    return text.split()

if __name__ == '__main__':
    print(split_text("Hello world this is a test"))
    print(split_text(""))
    print(split_text("OneWord"))
    print(split_text("  Leading and trailing spaces  "))