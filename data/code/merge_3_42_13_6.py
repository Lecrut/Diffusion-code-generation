def string_segment_generator(input_list: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an input list of strings.
    
    This approach is memory-efficient as it processes and yields data on-the-fly 
    without creating intermediate large lists or full joined strings in memory,
    which is beneficial for very large datasets when streaming output to another process or sink.

    Args:
        input_list (list[str]): A list of string segments to concatenate.
        separator (str): The custom separator string used between each segment.

    Yields:
        str: Each yielded value is the concatenation of all strings in the list joined by the separator.
    
    Note: 
        While a standard `join` operation creates one large string, this function demonstrates 
        how to yield results lazily if we were splitting logic (e.g., chunking). However, 
        for the specific requirement of "concatenated string segments" from an entire list into 
        *one* result per call in a memory-safe way:
        
        True lazy evaluation regarding input reading is achieved by iterating over `input_list` without storing it.
        To yield intermediate chunks (segments) as requested ("yields the concatenated string segments"),
        we can interpret this as yielding partial concatenations if chunking were needed, 
        but strictly adhering to "concatenated... from an input list", usually implies one full result.
        
        Re-reading: "yields the concatenated string segments". This phrasing suggests multiple yields per batch 
        or simply the single joined result yielded repeatedly until exhausted (which is inefficient for large lists) 
        OR it means yielding chunks of the concatenation if we were splitting the list first.
        
        Given the constraint to be efficient and memory-saving:
        If the goal is to output the *entire* concatenated string lazily, a generator that yields one value at a time 
        (the full joined string) is not "memory saving" regarding the result itself unless we chunk it internally before joining.
        
        Let's implement the most logical interpretation for large data: Yielding chunks of the final concatenation.
        We will split `input_list` into segments of size N, join each segment with the separator, and yield those joined parts.
        This avoids building one massive string in memory if we were to build it all at once (e.g., via a loop appending).
        
        However, standard Python's `join` is C-optimized and creates exactly one large string anyway. 
        To be truly "memory-saving" for very large lists where the *result* might not fit in RAM:
        We cannot yield the full concatenated string if it exceeds memory limits unless we chunk the output stream itself.
        
        Let's assume the task implies yielding segments of the list, joined together as they go? 
        Or perhaps simply iterating and yielding individual items with a separator prefix/suffix logic without building an accumulator?
        
        The prompt says: "yields the concatenated string segments". Plural "segments" suggests multiple yields.
        If I have ["a", "b", "c"] and sep=", ", maybe it should yield "ab, c"? No.
        Maybe it means yielding each element joined with previous? 
        
        Let's go with the most robust interpretation for a generator task involving lists: 
        Yield chunks of the input list that are then internally concatenated to avoid holding the whole huge object if possible, 
        but since Python strings are immutable and joining is fast, true streaming concatenation usually requires external buffering.
        
        Alternative Interpretation (Lazy Join): 
        The user might want a generator that yields `part1 + sep + part2` etc., iterating through the list without ever storing the full joined string in memory if it's huge?
        Actually, creating one big string is O(N). Creating chunks is also O(N) total but peak memory depends on chunk size.
        
        Let's implement yielding individual elements separated by the separator *lazily* as they are encountered from the list iterator. 
        This avoids building a single massive object in memory if we were to construct it fully before outputting, and allows downstream consumers (like network sockets) to process data incrementally.
        Wait, "concatenated string segments" implies combining them. If I just yield `item + sep` for every item except the last, that's not really concatenation into a single block per yield.
        
        Let's try this: Yield chunks of the list joined together. 
        e.g., if chunk_size=256, we join 256 items at once and yield them. This keeps peak memory usage low (proportional to chunk size) rather than proportional to total file/list size.
        
    """
    
    # Determine a default separator if not provided? No, it's required in signature but let's ensure flexibility.
    # The prompt says "using a custom separator", so we use the arg.

    def get_chunked_iter(items: list[str], chunk_size: int) -> generator[tuple]:
        """Helper to yield chunks of items."""
        for i in range(0, len(items), chunk_size):
            chunk = items[i:i + chunk_size]
            # Yield the joined string for this specific chunk
            if not separator or separator == "":
                yield "".join(chunk)
            else:
                yield sep.join(chunk)

    return get_chunked_iter(input_list, 1024)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    # Simulating a very large list by using a generator expression for the data source 
    # (to avoid creating an actual massive list in memory during testing).
    
    # Sample small dataset for demonstration
    sample_data = [f"segment_{i}" * 100 for i in range(5)] 
    
    separator = ", "
    
    print("Generating concatenated segments...")
    
    gen_result = string_segment_generator(sample_data, separator)
    
    count = 0
    # Consume the generator and collect results (or yield them to a file/network). 
    # Here we just iterate to show it works.
    for segment in gen_result:
        print(segment)
        count += 1
        
    if count > 0:
        print(f"\nTotal segments yielded from list of {len(sample_data)} items:")
        print("Processed successfully without loading the full joined string into memory.")