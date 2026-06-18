import sys
def compute_center_mark(sequence):
    try:
        length = len(sequence)
        if length == 0:
            return None
        mid_index = (length - 1) // 2
        return sequence[mid_index]
    except TypeError:
        raise ValueError("Input must be a sequence object")
if __name__ == '__main__':
    sample_sequences = [
        list(range(5)),                                                     
        tuple([10, 20, 30]),                   
        [],                                                    
        list(range(6)),                                                                    
    ]
    results = []
    for seq in sample_sequences:
        try:
            mark = compute_center_mark(seq)
            results.append(f"Sequence {seq} -> Center Mark: {mark}")
        except ValueError as e:
            results.append(f"Error with sequence type: {e}")
    print("\n".join(results))