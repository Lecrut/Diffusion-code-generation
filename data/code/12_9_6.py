def get_middle(sequence):
    n = len(sequence)
    if n == 0:
        raise ValueError("Sequence is empty")
    mid_index = n // 2
    return sequence[mid_index]

if __name__ == '__main__':
    odd_seq = [1, 2, 3, 4, 5]
    even_seq = [10, 20, 30, 40]
    
    print(get_middle(odd_seq))
    print(get_middle(even_seq))