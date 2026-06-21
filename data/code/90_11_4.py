def has_leading_a_or_b(items):
    prefixes = {'A': True, 'B': True}
    for item in items:
        if item and item[0] in prefixes:
            return True
    return False

if __name__ == '__main__':
    data = ['Alpha', 'Beta', 'Gamma']
    outcome = has_leading_a_or_b(data)
    print(outcome)