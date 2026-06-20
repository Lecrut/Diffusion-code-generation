def strip_whitespace(text):
    return text.strip()

if __name__ == '__main__':
    samples = {
        "basic": "  hello world  ",
        "tabs": "\t\n\t\n  spaces around  \t\n\t\n",
        "clean": "no leading or trailing whitespace",
        "empty": "   ",
        "mixed": " \t\r\n  content  \t\r\n "
    }
    for key, value in samples.items():
        print(strip_whitespace(value))