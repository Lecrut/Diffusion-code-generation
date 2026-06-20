def is_mutually_exclusive(triplet: tuple[bool, bool, bool]) -> bool:
    if not all(isinstance(x, bool) for x in triplet):
        raise ValueError("All elements must be boolean")
    return sum(triplet) == 1

if __name__ == '__main__':
    sample_triplet = (True, False, True)
    print(is_mutually_exclusive(sample_triplet))