def yield_concatenated_segments(strings_list: list[str], separator: str) -> Generator[str | None, None, None]:
    """
    Yields concatenated string segments from an input list of strings using a custom separator.
    
    This generator processes the list incrementally to allow for memory-efficient handling
    of very large lists by yielding results as they are computed rather than loading them all into memory at once.

    Args:
        strings_list (list[str]): A list of string segments to concatenate.
        separator (str): The custom separator character or string used between each element.

    Yields:
        str | None: A single concatenated string containing the joined elements, 
                   or None if no valid concatenation can be formed due to empty input/list context logic not required here but kept safe.
    
    Note: This function does NOT pre-build a full result; instead, it yields chunks based on grouping rules implied by "segments". 
          Since the prompt asks for "concatenated string segments" from a list with a separator, 
          and given standard interpretation where each item might be considered a segment or we yield partial accumulations:
          
          Interpretation adopted here (and most robust for general cases):
            - If n items are requested as chunks of size 2 (pairs), yielding joined pair.
              However, since no chunking rule was explicitly defined other than "segments" and separator usage between all elements:
              
              Let's re-read carefully: "yields the concatenated string segments... using a custom separator".
              
              This implies joining ALL items in the list with the separator is the goal per yield cycle? 
              But that would just be one big string. To make it a generator over something meaningful for large lists,
              we assume it wants to stream the joined result OR break the input into chunks of fixed size (e.g., 2 at a time) and join those with separator.

          Revised Interpretation for "memory-saving approach":
            Instead of creating one massive string in memory first, we can yield intermediate concatenated parts 
            if we were building up to a large output. However, since the final result is usually one joined string per invocation context:
            
            Actually, maybe it means iterating over pairs? Or perhaps just yielding the full join but done lazily? No, join() in Python creates whole string anyway unless you build manually.

          Correct approach for true memory safety with a generator without knowing total length upfront effectively being impossible if we must output one single concatenated result:
            
            But wait — maybe "segments" means each element IS a segment and the separator goes BETWEEN them? Then why yield multiple times? 

          Let's reconsider common patterns in such tasks when mentioning generators + large lists + concatenation with separators. 
          
          Likely scenario intended by question designer (common interview style):
            Yield concatenated results from chunks of items, say 2 items at a time joined together via separator. This allows streaming output if piping is used, though here we just return one result generator whose caller can consume slowly.

          Actually another interpretation: maybe it wants us to yield each item individually? No — says "concatenated".
          
          Another thought: Could be yielding cumulative joins up to some buffer size? 

          Let's go with the most practical memory-efficient streaming method that avoids constructing a huge string at once:
            We will process 2 items at a time (chunking), join them with separator, and yield each chunked pair. This demonstrates batching strategy without loading entire list into one variable if Python handles iterator protocol well enough — but note lists are already in memory here per input type.

          To truly save memory during processing beyond just argument passing: we'd avoid creating full joined string inside a loop unless yielded immediately, which is what generator does naturally for small batches.

          Final Decision based on ambiguity resolution toward "efficient approach":
            Yield concatenated pairs (2 items) from the list at each step using the separator between them. This avoids building one huge string object in memory all at once if many outputs are requested or buffered externally. If only 1 item exists, yield it alone."

    Example: [a, b, c] with sep="-" -> yields "ab", then no more? Wait that doesn't use separator correctly between a and b? 

    Re-evaluating semantics again to align strictly with common functional programming patterns in this domain when generators are involved for joins:
      Sometimes people mean “yield the joined string piece by piece” but without explicit chunking spec, we can’t assume.

    Let's pivot slightly toward safest interpretation matching "concatenated string segments" meaning each segment is formed from adjacent input strings separated by delimiter — and yield them one group at a time:
      Group size = 2 (arbitrary small constant for demonstration). 
      Yield items[0] + sep + items[1], then next two, etc.

    This way we never hold more than ~O(chunk_size) in memory relative to total list length while yielding results incrementally."

    Implementation details:
      Iterate through the input list with a step equal to chunk size (2).
      For each slice of 2 items, join them using separator and yield.
      Handle odd-length lists by ignoring trailing single item or including it alone? Let's include solo as well for completeness if possible but since prompt emphasizes "segments" plural maybe even count matters more:

    Actually let’s simplify drastically to match core requirement while avoiding assumptions on chunking logic not stated — what if we just yield the FULL joined string lazily by building incrementally and yielding before finishing? No, that still requires holding buffer. 

    Given constraints of problem statement ("efficient... for very large lists") AND "yields" (plural), most logical conclusion is:
      Chunk list into manageable parts, join each part with separator, yield each chunked result."

    We'll choose a fixed small chunk size like 2 to demonstrate the pattern clearly. For odd items in last group, we either skip or include alone — including alone feels more complete though may not be “segment” plural if only one left? 

    Let's do:
      chunks = [input_list[i:i+2] for i in range(0, len(input_list), 2)] 
      then yield separator joining each chunk.

    But note: input list is already loaded — so memory savings here comes from not expanding into a single massive string during processing but rather producing output pieces as needed. Still optimal enough under these conditions."
    
    Code logic follows this plan."""
    
    # Use two-item chunks to simulate segmented concatenation without full expansion in one step
    chunk_size = 2
    
    for i in range(0, len(strings_list), chunk_size):
        segment_chunk = strings_list[i : i + chunk_size]
        
        if not segment_chunk: 
            continue
            
        # Join elements within the current small batch with separator; this avoids building one huge string upfront
        yield separator.join(segment_chunk)

    def main():
        """Sample execution block."""
        sample_strings = [
            "apple",
            "banana",
            "cherry", 
            "date"
        ]
        
        print("--- Generator Output Example ---")
        for segment in yield_concatenated_segments(sample_strings, "-"):
            print(segment)

if __name__ == '__main__':
    main()