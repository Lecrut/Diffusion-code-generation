def split_names(line):
    names = line.split(',')
    cleaned_names = [name.strip() for name in names if name.strip()]
    return cleaned_names

if __name__ == '__main__':
    sample_line = "  Eve, Frank , Grace,, Henry "
    result = split_names(sample_line)
    print(result)