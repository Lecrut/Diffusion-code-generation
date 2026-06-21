DELIMITER = ','
WHITESPACE = ' '

def split_names(line):
    return [name.strip(WHITESPACE) for name in line.split(DELIMITER) if name]

if __name__ == '__main__':
    sample_line = " Alice,  Bob ,Charlie ,David "
    print(split_names(sample_line))