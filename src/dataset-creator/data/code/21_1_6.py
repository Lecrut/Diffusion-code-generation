import sys
def append_to_immutable(seq):
    if isinstance(seq, (list, tuple)):
        new_seq = seq + (seq[-1],) if len(seq) > 0 else ()
        return new_seq
    elif hasattr(seq, '__iter__'):
        items = list(seq)
        new_list = items + [items[-1]]
        return tuple(new_list)
    raise TypeError("Input must be an iterable sequence")
if __name__ == '__main__':
    sample_data = (10, 20, 30)
    result = append_to_immutable(sample_data)
    print(result)