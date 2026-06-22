def find_middle(tup):
    if not tup:
        raise ValueError("Empty sequence has no middle element")
    return tup[len(tup) // 2]

if __name__ == '__main__':
    sample = (1, 2, 3, 4, 5)
    result = find_middle(sample)
    print(result)