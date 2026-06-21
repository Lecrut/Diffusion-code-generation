def contains_a_or_b_start(strings):
    prefix_map = {'A': 'Alpha', 'B': 'Beta'}
    valid_starts = tuple(prefix_map.keys())
    for text in strings:
        if text and text[0] in valid_starts:
            return True
    return False

if __name__ == '__main__':
    words = ['Avocado', 'Banana', 'Cherry']
    found = contains_a_or_b_start(words)
    print(found)