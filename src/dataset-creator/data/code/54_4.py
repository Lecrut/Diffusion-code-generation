import collections
def compute_center_mark(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Sequence must be list or tuple")
    length = len(sequence)
    if length == 0:
        return None
    index = length // 2
    return {"index": index, "value": sequence[index]}
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ('a', 'b', 'c')
    result_list = compute_center_mark(sample_list)
    print(result_list)
    result_tuple = compute_center_mark(sample_tuple)
    print(result_tuple)