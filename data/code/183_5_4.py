def split_names(line):
    return [name.strip() for name in line.split(',') if name.strip()]

if __name__ == '__main__':
    sample_line = ' Alice,  Bob ,Charlie ,David '
    print(split_names(sample_line))