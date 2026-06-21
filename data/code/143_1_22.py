def has_contradictory_pairs(propositions):
    seen = set()
    for prop in propositions:
        if not prop:
            continue
        if -prop in seen:
            return True
        seen.add(prop)
    return False

if __name__ == '__main__':
    sample_values = [1, -1, 2, 3, -2]
    print(has_contradictory_pairs(sample_values))