def has_true_at_least_once(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    
    class TrueFinder:
        def __init__(self, source):
            self.source = iter(source)
            self.found = False
            
        def __iter__(self):
            return self
            
        def __next__(self):
            if self.found:
                raise StopIteration
            try:
                item = next(self.source)
                if item:
                    self.found = True
                    return True
                return False
            except StopIteration:
                if self.found:
                    raise StopIteration
                raise

def check_sequence_bools(seq):
    if not isinstance(seq, (list, tuple)):
        raise TypeError("Sequence must be list or tuple")
    if not all(isinstance(x, bool) for x in seq):
        raise ValueError("All elements must be booleans")
    
    finder = TrueFinder(seq)
    for val in finder:
        if val:
            return True
    return False

if __name__ == '__main__':
    test_seq1 = [False, False, True, False]
    test_seq2 = [False, False, False]
    test_seq3 = [True, False, True]
    
    result1 = check_sequence_bools(test_seq1)
    result2 = check_sequence_bools(test_seq2)
    result3 = check_sequence_bools(test_seq3)
    
    print(result1)
    print(result2)
    print(result3)