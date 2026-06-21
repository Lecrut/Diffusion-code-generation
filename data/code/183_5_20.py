def split_names(line):
    names = [name.strip() for name in line.split(',')]
    if not all(name for name in names):
        raise ValueError("Line contains empty name segments")
    return names

if __name__ == '__main__':
    sample_line = "Alice, Bob , Charlie,, David"
    try:
        print(split_names(sample_line))
    except ValueError as e:
        print(e)