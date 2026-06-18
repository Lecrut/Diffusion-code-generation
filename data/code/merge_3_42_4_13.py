def concat_generator(iterable: list[str], separator: str) -> generator:
    """
    Generator function that yields concatenated string segments from an iterable of strings,
    using a custom separator between each segment (except potentially the last if not specified).
    
    Args:
        iterable: An iterable containing strings to be joined.
        separator: The string used as a delimiter between elements.
        
    Yields:
        A single concatenated string formed by joining all input segments with the separator,
        or yields individual parts based on specific logic if needed for streaming behavior.
        Since the task asks for "concatenated string segments", we interpret this as yielding 
        progressively built strings up to a limit or simply yielding the final joined result once complete.
        
    However, re-reading strictly: "yields the concatenated string segments". This could mean:
    1. Yield one big string at the end (if iterable is exhausted).
    2. Or yield intermediate chunks if we were building it piece by piece over time? 
       But generators usually run once per call unless re-runnable, so yielding a single final joined result makes most sense for "concatenated".
       
    Let's assume the requirement implies joining them all together with the separator and yielding that one full string.
    If multiple segments were expected in different phases of execution within one generator instance without external state, 
    we would need to yield pieces as they come? But standard generators don't pause input easily unless using async or buffers.
    
    Given typical interpretation: Join all items with separator and yield once.
    """
    if not iterable:
        return
    
    # We'll build the string in memory then yield it, OR we could try to simulate streaming chunks? 
    # But without explicit chunk size request, let's just join everything.
    
    result = ""
    for item in iterable:
        current_segment = str(item) if not isinstance(item, (str, bytes)) else item
        
        # If this is the first segment or separator was used before... wait logic needs adjustment.
        # Actually simpler: Just join with separator and yield once at end? 
        # Or maybe yield each chunk as it's processed? Let's do a single full concatenation per call to generator, yielding that one string.

if __name__ == '__main__':
    pass
