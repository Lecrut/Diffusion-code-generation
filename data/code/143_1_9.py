def has_contradictory_pairs(propositions):
    seen = set()
    for prop in propositions:
        if prop in seen:
            return True
        seen.add(not prop)
    return False

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(has_contradictory_pairs(sample_values))