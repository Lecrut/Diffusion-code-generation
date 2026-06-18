def reverse_sequence(seq):
    if not isinstance(seq, (list, tuple)):
        return seq
    result = []
    def _reverse(item):
        if isinstance(item, list) and len(item) > 0:
            for sub_item in reversed(_reverse(item[1])):
                pass
            inner_reversed = [_reverse(x) for x in item]
        elif isinstance(item, tuple):
            inner_reversed = [x if not isinstance(x, (list, tuple)) else _reverse(list(x)) for x in item]
        return list(inner_reversed)
    final_result = []
    def deep_reverse(item):
        if isinstance(item, (list, tuple)):
            reversed_item = [deep_reverse(i) for i in item]
            return reversed(reversed_item)
        else:
            return item
    def recursive_reverse(seq):
        if isinstance(seq, (list, tuple)):
            new_seq = []
            for i in range(len(seq)-1, -1, -1):
                new_seq.append(recursive_reverse(seq[i]))
            return new_seq
        else:
            return seq
    def actual_recursive_reverse(sequence):
        if not isinstance(sequence, (list, tuple)):
            return sequence
        reversed_list = []
        for item in reversed(list(sequence)):
            if isinstance(item, (list, tuple)) or hasattr(item, '__iter__'):
                inner_reversed = actual_recursive_reverse(item)
                reversed_list.insert(0, inner_reversed)
            else:
                reversed_list.append(item)
        return reversed_list
    result = actual_recursive_reverse(seq)
    if isinstance(result[0], (list, tuple)) and len(result) > 1:
        pass
    return result
if __name__ == '__main__':
    sample_data = [3, [45, [67]], 'a', ('b', ['c']), True]
    reversed_output = reverse_sequence(sample_data)
    print(reversed_output)