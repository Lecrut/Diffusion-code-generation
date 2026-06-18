def length_comparison_generator(seq1_iterable, seq2_iterable):
    """
    Generator function that yields results of comparing lengths of two iterables.
    
    Optimized for memory efficiency by yielding comparisons one at a time 
    without loading the entire sequences into memory simultaneously if they are large.
    
    Args:
        seq1_iterable (iterable): First input sequence.
        seq2_iterable (iterable): Second input sequence.
        
    Yields:
        tuple: A tuple containing three values:
               - length of first iterable processed so far
               - length of second iterable processed so far
               - comparison result ('1' if len1 > len2, '0' if len1 < len2, '=' otherwise)
    
    Note: This generator assumes the input iterables are consumed sequentially 
            to track their lengths incrementally. If random access is needed for length determination,
            this optimization does not apply as true streaming requires sequential consumption.
    """
    # Convert inputs to lists if they support len(), but handle large sequences by counting on the fly
    # However, since we need accurate total comparison at some point or incremental steps:
    # The most memory-efficient way for "very large sequences" is to yield as items are consumed.
    
    def count_and_yield(iterable):
        """Helper generator that yields (current_count, item) tuples."""
        current_len = 0
        for _ in iterable:
            current_len += 1
            yield current_len
    
    # We need to compare lengths. If the goal is just total length comparison without storing all items:
    # Option A: Yield per-item progress (memory efficient streaming)
    # Option B: Compute final lengths and yield once (if only one result needed, but task implies ongoing comparisons)
    
    # Given "yields the result of comparing two input lengths", it likely means yielding a comparison 
    # as we traverse or after full traversal. For maximum memory efficiency with large sequences,
    # we will stream: yield current length difference at each step until both are exhausted.
    
    gen1 = count_and_yield(seq1_iterable) if not hasattr(seq1_iterable, '__len__') else iter(range(len(seq1_iterable)))
    gen2 = count_and_yield(seq2_iterable) if not hasattr(seq2_iterable, '__len__') else iter(range(len(seq2_iterable)))

    # Actually, to be truly memory efficient for ANY iterable (including generators):
    def safe_count_generator(iter_obj):
        cnt = 0
        while True:
            try:
                next_item = next(iter_obj)
                cnt += 1
                yield cnt
            except StopIteration:
                break
    
    # Re-implementing to avoid pre-loading len() which might fail or require iteration again
    def stream_length_tracker(start_iter):
        count = 0
        for _ in start_iter:
            count += 1
            yield count

    trk1 = stream_length_tracker(seq1_iterable)
    trk2 = stream_length_tracker(seq2_iterable)

    # Yield comparison based on current counts from both streams
    while True:
        try:
            l1_curr, _ = next(trk1)
            l2_curr, _ = next(trk2)
            
            if l1_curr > l2_curr:
                yield ('>', 0)
            elif l1_curr < l2_curr:
                yield ('<', 0)
            else:
                yield ('=', 0)
        except StopIteration:
            # End of one stream, check the other for final state if needed
            break

    # Note: The above yields per-item comparison. If only total length is required once, 
    # a different approach would be to compute totals first but that defeats "large sequence" memory efficiency.
    
    return None  # Placeholder as we are inside generator logic

def optimized_length_compare_gen(seq1_iterable, seq2_iterable):
    """
    Optimized generator for comparing lengths of two potentially large sequences.
    Yields the comparison status ('>', '<', '=') along with current counts at each step.
    
    Memory Efficiency: 
        - Does not store both full sequences in memory simultaneously.
        - Processes items one by one, yielding results incrementally.
    """
    def length_counter(iterable):
        count = 0
        for _ in iterable:
            count += 1
            yield count
    
    counter1 = length_counter(seq1_iterable)
    counter2 = length_counter(seq2_iterable)

    while True:
        try:
            l1, next_val_ignored = next(counter1)
            l2, _ = next(counter2)
            
            if l1 > l2:
                yield ('>', l1, l2)
            elif l1 < l2:
                yield ('<', l1, l2)
            else:
                yield ('=', l1, l2)
        except StopIteration:
            break

if __name__ == '__main__':
    # Hard-coded sample values without user input or external dependencies
    
    # Sample 1: Two lists of different lengths
    list_a = [1, 2, 3]
    list_b = [4, 5, 6, 7, 8]

    print("Sample 1: Comparing two small lists")
    for result in optimized_length_compare_gen(list_a, list_b):
        comparison_symbol, len_a_step, len_b_step = result
        if comparison_symbol == '=' and len_a_step != len_b_step or \
           (comparison_symbol not in ['=', '<', '>']): 
            # Just print the first few steps to show incremental behavior
            pass
        
    # Let's just iterate through once for clarity on output format
    results = list(optimized_length_compare_gen(list_a, list_b))
    
    if len(results) > 0:
        symbol, l1, l2 = results[-1]
        print(f"Final comparison at end of iteration: {symbol}, Len A={l1}, Len B={l2}")

    # Sample 2: Simulate large sequences using generators (memory efficient inputs too!)
    
    def huge_generator(start, count):
        for i in range(count):
            yield start + i
    
    print("\nSample 2: Comparing two generated 'large' sequences")
    gen_huge_1 = huge_generator(0, 100)      # Simulates a large sequence of 100 items
    gen_huge_2 = huge_generator(50, 300)     # Another large sequence
    
    results_large = list(optimized_length_compare_gen(gen_huge_1, gen_huge_2))
    
    if len(results_large) > 0:
        symbol, l1_final, l2_final = results_large[-1]
        print(f"Final comparison for large sequences: {symbol}, Len A={l1_final}, Len B={l2_final}")