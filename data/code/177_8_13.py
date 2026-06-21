def split_text(text):
    return text.split()

if __name__ == '__main__':
    print(split_text("Hello World"))
    print(split_text(""))
    print(split_text("  Leading and trailing spaces  "))