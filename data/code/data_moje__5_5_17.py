def compare_lengths(seq1, seq2):
    iterator1 = iter(seq1)
    iterator2 = iter(seq2)
    
    while True:
        item1, item2 = None, None
        try:
            item1 = next(iterator1)
        except StopIteration:
            item1 = None
        try:
            item2 = next(iterator2)
        except StopIteration:
            item2 = None
            
        if item1 is None and item2 is None:
            break
        
        length1 = len(seq1) if hasattr(seq1, '__len__') else 0
        length2 = len(seq2) if hasattr(seq2, '__len__') else 0
        
        if length1 > 0 and length2 > 0:
            yield length1 > length2
        elif length1 > 0:
            yield True
        elif length2 > 0:
            yield False
        else:
            break

if __name__ == '__main__':
    results = list(compare_lengths([1, 2, 3], [1, 2]))
    print(results)