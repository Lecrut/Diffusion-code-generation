def compare_consecutive_elements(tup):
    return {frozenset(pair): pair[0] < pair[1] for pair in zip(tup, tup[1:])}

if __name__ == '__main__':
    sample_tuple = (3, 5, 2, 8, 6)
    print(compare_consecutive_elements(sample_tuple))