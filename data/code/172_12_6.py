def align_pairs(keys, tokens):
    return dict(zip(keys, tokens))

if __name__ == '__main__':
    keys = [1, 2, 3]
    tokens = ['a', 'b', 'c']
    print(align_pairs(keys, tokens))