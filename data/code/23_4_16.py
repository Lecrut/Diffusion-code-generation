def compare_sequences(seq1: list, seq2: list) -> generator:
    """
    Generator function that yields comparison results between pairs of values 
    from two input sequences based on their indices.
    
    Yields strings indicating whether the current pair is 'A is greater', 
    'B is smaller' (equivalent to A > B), or 'Equal'. If lengths differ, it stops at the shorter length.
    """
    for i in range(min(len(seq1), len(seq2))):
        val_a = seq1[i]
        val_b = seq2[i]

        if val_a > val_b:
            yield f"A is greater"
        elif val_b > val_a:
            yield "B is smaller"
        else:
            yield "Equal"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files)
    sequence_a = [10, 5, 3, 8]
    sequence_b = [2, 7, 9, 4]

    print("Comparison Results:")
    for result in compare_sequences(sequence_a, sequence_b):
        print(result)