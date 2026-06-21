def has_contradictory_pairs(propositions):
    seen = set()
    for prop in propositions:
        if not prop:
            continue
        inverse = not prop
        if inverse in seen:
            return True
        seen.add(prop)
    return False

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(has_contradictory_pairs(sample_values))