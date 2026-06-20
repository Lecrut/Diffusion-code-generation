def check_mutual_exclusivity(flags):
    return flags & flags - 1 == 0
if __name__ == '__main__':
    sample_flags = 5
    print(check_mutual_exclusivity(sample_flags))