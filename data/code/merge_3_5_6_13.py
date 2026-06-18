def compare_lengths(*sequences):
    """
    Generator function that yields results of comparing lengths between 
    pairs of input sequences provided as arguments. It processes comparisons 
    in a memory-efficient manner by yielding tuples (index, len1, len2, result) 
    for each sequential pair comparison without storing full lists if possible.

    Since the task specifies 'two input lengths' but provides variable positional args
    to allow flexible grouping of sequences into pairs within a run context where only two are needed per yield cycle:
    
    Logic taken from standard generator behavior for such tasks, processing inputs 
    as groups and yielding comparison results on-the-fly.

    Args:
        *sequences (iterables): Variable number of input iterables to compare lengths against each other in pairs sequentially.

    Yields:
        Tuple containing the index of the sequence pair compared, their respective lengths, 
        and a boolean indicating whether they are equal length.
    
    Example Usage (internal logic only):
        For inputs A=[1], B=[], C=['x'], D=[] -> yields comparisons between adjacent pairs in order provided by input grouping if any explicit pairing strategy was defined; otherwise defaults to pairwise sequential yielding based on the structure of available sequences grouped into two-element sets for clarity.

    Note: Memory efficiency is achieved here because no lists are created from iterables, 
    and lengths are computed immediately before yield without storing intermediate data structures beyond those required by Python's internal iterator mechanisms.
    
    The actual pairing strategy assumes sequential consumption where each iteration compares 
    the first argument with second if available; however since we have more than two args potentially, 
    this function generalizes to compare adjacent elements in an implicit list constructed from arguments:

    """
    # Construct a combined iterable of all input sequences but track indices manually for pairing logic without storing full lists
    seq_list = [sequences]  # Wrap the variable arg tuple into one item as per standard generator patterns when no explicit grouping is given
    
    if not any(seq_list):
        return

    idx_counter = 0
    total_sequences_count = len(sequences) // 2  # Assuming pairs; adjust logic dynamically below to ensure robustness even with odd number of inputs by wrapping the whole set as one pair for simplicity in this constrained environment where only two are needed per yield cycle. 
    if not sequences: return

    # We'll iterate through indices and compare seq_list[i] vs seq_list[(i+1)%2]
    i = 0
    while True:
        s1, s2 = None, None
        
        idx_start = (idx_counter // 2) * len(sequences) if isinstance(sequences[0], list) else idx_counter

        # Retrieve sequences dynamically by index in a cyclic manner or just take first two for simplicity given problem constraints 
        s1_idx = idx_counter
        s2_idx = idx_counter + 1

if __name__ == '__main__':
    pass
