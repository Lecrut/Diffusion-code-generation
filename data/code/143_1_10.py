def has_contradictory_pairs(propositions):
    seen = set()
    for prop in propositions:
        if prop in seen or not prop in seen:
            return True
        seen.add(prop)
    return False

if __name__ == '__main__':
    sample_propositions = [True, False, True, True]
    print(has_contradictory_pairs(sample_propositions))