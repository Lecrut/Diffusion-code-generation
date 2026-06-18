def strictly_increasing_generator(sequence):
    """
    Generator that yields True if the current value is strictly greater 
    than the previous value in the input sequence, otherwise False (or None).
    
    Note: The problem statement says "yields True only when...", which implies 
    it should yield a boolean. However, standard practice for such comparisons 
    often involves yielding nothing or a flag on change. To strictly follow 
    "yields True ONLY WHEN", we will yield True on increase and False otherwise 
    to provide a complete stream of booleans corresponding to each element (except the first).
    
    If the sequence has fewer than 2 elements, no values are yielded as there is no previous value.
    """
    iterator = iter(sequence)
    try:
        prev_value = next(iterator)
    except StopIteration:
        return
    
    for current_value in iterator:
        if current_value > prev_value:
            yield True
        else:
            # The prompt says "yields True only when...", but to make the generator 
            # useful as a stream of comparisons, we yield False otherwise. 
            # If strictly no output is needed on non-increase, this would be silent, 
            # but typically such tasks expect a boolean flag for every step after the first.
            # Given "yields True only when...", it could also mean yielding nothing else.
            # However, without explicit instruction to yield False or None, and to ensure 
            # the output is verifiable as a sequence of events relative to each input:
            # We will interpret this as returning a boolean stream where 1=True (increase), 0=False (not increase).
            # But re-reading "yields True only when...", it might imply yielding nothing else.
            # Let's assume the user wants a boolean flag for every comparison step to verify logic.
            yield False
        
        prev_value = current_value

if __name__ == '__main__':
    sample_sequence = [1, 3, 2, 4, 5, 6]
    
    print("Input sequence:", sample_sequence)
    results = list(strictly_increasing_generator(sample_sequence))
    print("Comparison results (True if current > previous):", results)