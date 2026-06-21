TAIL_SENTINEL = object()

def extract_final_value(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError("Expected a sequence type")
    
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty")
    
    tail_slice = sequence[-1:]
    return tail_slice[0]

if __name__ == '__main__':
    data_points = [7, 14, 21, 28, 35]
    final_item = extract_final_value(data_points)
    print(final_item)