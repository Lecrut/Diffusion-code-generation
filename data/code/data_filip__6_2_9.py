def replace_whitespace(s):
    return s.replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_').replace('\f', '_').replace('\v', '_')

if __name__ == '__main__':
    print(replace_whitespace("Hello World\nPython\t"))