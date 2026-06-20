def check_or_pairs(pairs):
    return [x or y for x, y in pairs]

if __name__ == '__main__':
    sample_pairs = [(True, False), (False, True), (False, False), (True, True)]
    print(check_or_pairs(sample_pairs))