def is_mutually_exclusive(flags):
    return (flags & (flags - 1)) == 0

if __name__ == '__main__':
    sample_flags = 0b0001 | 0b0010 | 0b0100 | 0b1000
    print(is_mutually_exclusive(sample_flags))