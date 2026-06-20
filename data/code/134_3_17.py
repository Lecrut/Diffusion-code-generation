def check_mutual_exclusivity(triplet: tuple[bool, bool, bool]) -> bool:
    return sum(triplet) == 1

if __name__ == '__main__':
    sample_triplet = (False, True, False)
    result = check_mutual_exclusivity(sample_triplet)
    print(result)