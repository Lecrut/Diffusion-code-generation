def has_contradictory_pairs(propositions):
    pairs = set()
    for prop in propositions:
        if not prop:
            continue
        pair = (prop, not prop)
        if pair in pairs:
            return True
        pairs.add(pair)
    return False

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(has_contradictory_pairs(sample_values))