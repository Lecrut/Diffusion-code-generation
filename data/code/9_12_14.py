def trim_string(text):
    return text.strip()

if __name__ == '__main__':
    print(trim_string('  hello world  '))
    print(trim_string('\t\n spaces \n\t'))
    print(trim_string('no_trim_needed'))