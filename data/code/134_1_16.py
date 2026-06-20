def check_mutual_exclusivity(flags):
    return (flags & (flags - 1)) == 0

if __name__ == '__main__':
    sample_flags = 0b00000010
    print(check_mutual_exclusivity(sample_flags))