def compare_lengths(seq1, seq2):
    len1 = iter(len(chunk) for chunk in seq1)
    len2 = iter(len(chunk) for chunk in seq2)
    
    while True:
        try:
            l1 = next(len1)
        except StopIteration:
            yield -1
            break
        
        try:
            l2 = next(len2)
        except StopIteration:
            yield 1
            break
        
        if l1 < l2:
            yield -1
        elif l1 > l2:
            yield 1
        else:
            yield 0

if __name__ == '__main__':
    seq1 = ['abc', 'defg', 'hijkl']
    seq2 = ['abcd', 'ef', 'ghi', 'jklm']
    
    result = compare_lengths(seq1, seq2)
    for comparison in result:
        print(comparison)