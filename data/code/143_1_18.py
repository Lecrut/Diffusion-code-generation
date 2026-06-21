def has_contradictory_pairs(propositions):
    positive = set()
    negative = set()
    for prop in propositions:
        if prop:
            positive.add(id(prop))
        else:
            negative.add(id(prop))
    return not positive.isdisjoint(negative)

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(has_contradictory_pairs(sample_values))