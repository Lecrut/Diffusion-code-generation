def replace_whitespace_with_underscores(s):
    return s.replace(' ', '_').replace('\t', '_').replace('\n', '_').replace('\r', '_').replace('\f', '_').replace('\v', '_')

if __name__ == '__main__':
    sample = "Hello World\tNew\nLine"
    result = replace_whitespace_with_underscores(sample)
    print(result)