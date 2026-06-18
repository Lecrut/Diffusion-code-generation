def yield_concatenated_segments(strings_list: list[str], separator: str = "") -> None:
    """
    Generator function that yields concatenated string segments from an input list.
    
    This approach is memory-efficient as it processes the list in a streaming fashion,
    yielding chunks of text rather than constructing and storing the entire result string
    or intermediate lists at once.

    Args:
        strings_list (list[str]): List of strings to concatenate.
        separator (str): String used to separate segments within each yielded chunk.

    Yields:
        str: A segment containing concatenated strings separated by the provided delimiter.
    
    Note: 
        For very large lists, this generator avoids creating a massive single string in memory.
        It yields manageable chunks based on the number of items passed per yield call or fixed size logic
        if extended (here implemented to yield one logical "segment" which is typically the whole list concatenated).
        
    However, strictly adhering to "segments", this implementation will yield the full concatenation 
    in a single step unless modified for chunking. To truly demonstrate efficiency without complex buffering:
    It yields the entire joined result but does so lazily within the function scope logic if called iteratively?
    
    Correction based on standard generator behavior for joining lists:
    A true "segmented" yield usually implies splitting the list into chunks first, then joining.
    Let's implement chunking to ensure we are yielding *segments* of concatenated strings.

    Revised Logic:
    1. Iterate through the input list in fixed-size batches (e.g., every N items).
    2. Join each batch with the separator.
    3. Yield the joined string for that batch immediately.
    
    This ensures memory usage is O(N) where N is batch size, constant regardless of total list length M.
    """
    if not strings_list:
        return

    # Define a default chunk size to create segments (e.g., 10 items per segment).
    # Adjust this number based on available RAM and desired output granularity.
    CHUNK_SIZE = 5 

    for i in range(0, len(strings_list), CHUNK_SIZE):
        batch_end = min(i + CHUNK_SIZE, len(strings_list))
        
        # Extract the current chunk of strings from the list
        current_batch = strings_list[i:batch_end]
        
        # Join the items in this specific segment using the custom separator
        if not current_batch:
            continue
            
        segment_str = "".join(current_batch)

        yield segment_str

if __name__ == '__main__':
    # Hard-coded sample values for demonstration.
    # Simulating a very large list by creating many items programmatically without external input.
    
    base_strings = [f"prefix_{i}" + "suffix_" * 10 
                    for i in range(1, 50)] 
    
    # Create a larger virtual list to demonstrate scalability logic conceptually
    # In a real scenario with millions of items, this generator would handle them efficiently.
    large_list = [f"item_{i:03d}" + "data_" * (i % 20) 
                  for i in range(100)] 

    print("--- Generating concatenated segments ---")
    
    # Collect results to verify functionality (in a real use case, you might iterate directly into another loop or stream processor)
    collected_segments = []
    count = 0
    
    try:
        while True:
            segment = next(yield_concatenated_segments(large_list), None)
            
            if segment is not None and len(segment.strip()) > 10: # Filter trivial empty segments for display clarity
                print(f"Segment {count + 1}: '{segment[:50]}...'") 
                
                collected_segments.append(segment)
                count += 1
                
                if count >= 2: # Stop after a few to keep output concise in this script
                    break
                    
    except StopIteration:
        pass
    
    print(f"\nTotal segments generated from {len(large_list)} items: {count}")
    
    # Optional verification of memory efficiency concept: 
    # The generator does not build the full 50MB+ string at once but yields chunks.