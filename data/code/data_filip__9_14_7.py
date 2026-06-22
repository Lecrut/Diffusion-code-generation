def strip_whitespace(s):
    return s.strip()

if __name__ == '__main__':
    print(strip_whitespace('  hello world  '))
    print(strip_whitespace('\t\nfoo\n\t'))
    print(strip_whitespace('   '))
    print(strip_whitespace('no_spaces'))
    print(strip_whitespace(''))