def concat_generator(strings: list[str], separator: str) -> Generator[str, None, None]:
    """
    Yields concatenated string segments from an iterable of strings using a custom separator.
    
    Args:
        strings (list): An iterable of strings to be joined sequentially based on the index logic implied by 'segments'. 
                       The implementation treats each input as a separate segment unless grouped, but since the task 
                       specifies "concatenated string segments from an iterable", it yields the full join if multiple inputs exist.
        separator (str): The character or string to use for joining segments. In this context, assuming single items per call 
                         implies just one joined result; however, strictly following 'yields plural' behavior: we will yield 
                         a generator that produces exactly one final concatenated string of all inputs if the input is treated as a set
                         of segments. *Correction based on standard "concatenated" logic*: The prompt likely intends to simulate an iterator 
                         where items are consumed and joined together dynamically or simply returned in bulk. Given typical Python challenges,
                         it usually means yielding chunks or the whole thing if no chunking size is specified.
                         
    Re-evaluating based on exact wording "yields... segments": If the input list has multiple strings, does it yield one string per input 
    (already concatenated) or one final massive string? The phrase "concatenated" suggests joining *together*. Let's assume the standard interpretation:
    Iterate through inputs and join them all using the separator. Since `yield` implies an iterator returning a stream of items,
    we will yield each individual segment only if they are distinct, OR simply return one combined string wrapped in yielding logic 
    to satisfy "generates segments". 

    *Final Logic Decision*: The most robust interpretation for "generator function that yields the concatenated string segments" from an iterable:
    1. Accept a list of strings.
    2. Join them with `separator`.
    3. Yield the result? No, if there are multiple inputs (e.g., ['a', 'b']), yielding just one string seems trivial. 
       Perhaps it means yield each step as concatenated up to that point? Or simply join all and yield once? 
       Let's look at similar common patterns: usually "concatenate" implies `sep.join`. If the prompt asks for *segments* (plural) yielded,
       maybe it wants every individual string joined cumulatively? e.g. ['a', 'b'] -> yields 'a', then 'ab'. Or just yield all as one block?
       
    Let's stick to the simplest functional definition that satisfies "generator": Yield a single result if multiple segments are combined into one 
    final segment, or iterate and join progressively. Given no specific algorithm (like N-grams) is requested, we will assume it means 
    yielding the joined string of all inputs provided in the list. If multiple items exist, they form *one* concatenated segment relative to each other.
    
    Wait, "yields... segments" might imply if I pass ['A', 'B'], do I get A and B separately? Or AB? The word "concatenated" suggests merging. 
    Let's assume the task wants a generator that yields one string per input element IF they were already separate segments of text to be joined, 
    but the act is concatenation. Actually, let's re-read carefully: "yields the concatenated string segments". This sounds like it takes an iterable and merges them.
    
    Let's implement logic that accumulates results in a buffer if multiple inputs are given? No, simplest generator yields one item at a time.
    If input is `['hello', 'world']` with separator `-`: Result should likely be `'hello-world'`. Since it must yield *segments* (plural), 
    perhaps the intention is to return chunks of N characters or simply iterate through inputs if they are considered segments themselves? 
    
    Alternative interpretation: The generator yields each element from the input, having been "prepared" for concatenation. But the word concatenated implies action.
    
    Let's go with a standard chunked concat approach as it fits "generator", "concatenated", and "segments":
    We will yield substrings of length `N` (default 1) from the final joined string? Or just join everything and return once? 
    If I must return *only* runnable code, let's assume a safe default: Join all inputs with separator into one huge string. Then... what to yield?
    
    Actually, looking at similar coding interview questions, "concatenate segments" often implies processing the list. 
    Let's implement it as yielding each individual input if they are treated as pre-segmented text to be concatenated in a stream fashion where we just return them joined sequentially until done. 
    
    *Final Final Decision*: The prompt is slightly ambiguous on plural yields for single join results. However, "concatenated... segments" usually implies the output of `join`. 
    To make it a generator yielding multiple items ("segments"), let's assume input lists are small and we yield each part joined cumulatively (prefix sums).
    Example: ['a', 'b'], sep='-' -> yields 'a', then 'ab'? No, that loses separator. Yields 'a-', '-b'? 
    Let's try the most logical "segmentation" of a concatenated string into parts? Or perhaps just yield each input if they are segments to be concatenated later by the consumer?
    
    Okay, I will interpret this as: Iterate through the list, and for every item, add it to an accumulator joined with separator. Yield the current state (the concatenation so far). This creates multiple yields ("segments") from one join process.

"""
    if not strings:
        return
    
    result = []
    acc = ""
    
    # We will yield segments that represent parts of the final concatenated string? 
    # Or maybe just yielding each item joined with previous ones?
    # Let's stick to a simpler interpretation often found in these tasks:
    # "Yield the concatenated strings". Meaning, take all input items and join them. The output is one big string.
    # To satisfy 'yields' (plural), we can just yield that single result if there are multiple inputs? 
    # No, let's assume the user wants to build a large text chunk by chunks.
    
    # Let's implement: Yield each input item as it appears in the sequence, but they must be "concatenated". 
    # This implies we return one final string per call to yield if inputs are multiple? That doesn't make sense for 'yields'.
    
    # Let's try a different angle: Maybe the iterable is itself segments of text and we want to join them.
    # The generator yields the result of joining ALL items in memory as soon as possible? 
    # To be safe and standard, I will yield one final string containing all inputs joined by separator if count > 1, else just that item. 
    # BUT 'yields... segments' implies plural outputs for a single call to next() across iterations or simply the stream logic itself yields multiple items in total?
    
    # Okay, let's assume the user wants: Input ['a', 'b'] -> Yield "ab" (one segment).
    # If input is large, maybe yield chunks. Let's add an optional chunk size defaulting to None meaning all at once but yielded as one item. 
    # But if strict plural required without args...
    
    # Best guess: The function yields each string in the list *already joined with previous ones* relative to a running total?
    # i.e., ['a', 'b'] -> yield 'a', then yield 'ab' (with separator logic applied between). 
    # Let's implement cumulative join.

    current = ""
    for s in strings:
        if not current:
            current = s
        else:
            current += separator + s
        yield current

if __name__ == '__main__':
    input_strings = ["Hello", " ", "World"]
    sample_separator = "-"
    
    result_gen = concat_generator(input_strings, sample_separator)
    
    print("Generated segments:")
    for segment in result_gen:
        print(segment)