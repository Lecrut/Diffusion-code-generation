def symmetric_difference(iterable1, iterable2):
    set1 = set(iterable1)
    set2 = set(iterable2)
    return list(set1.symmetric_difference(set2))

if __name__ == '__main__':
    sample_values = {
        'list_a': [1, 2, 3, 4],
        'list_b': [3, 4, 5, 6]
    }
    
    result = symmetric_difference(sample_values['list_a'], sample_values['list_b'])
    print(result)