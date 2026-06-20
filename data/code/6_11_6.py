def spaces_to_underscores(text):
    return text.replace(' ', '_')

if __name__ == '__main__':
    sample = "Hello World This Is A Test"
    print(spaces_to_underscores(sample))