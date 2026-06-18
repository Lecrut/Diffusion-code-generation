def yield_concatenated_strings(strings_list, separator):
    """
    Generator function that yields concatenated string segments from an iterable of strings.
    
    Args:
        strings_list (iterable): An iterable containing individual string elements to be concatenated.
        separator (str): The custom string used as a delimiter between the original segments when yielding them combined? 
                         Wait, re-reading task: "yields the concatenated string segments".
                         Usually this means grouping by index or just joining all of them.
                         Let's interpret "concatenated string segments" as taking every Nth element and concatenating them into a single chunk to yield one-by-one? 
                         
                         Actually, simpler interpretation often intended in such tasks: 
                         Yield the full concatenated result if it was once joined, OR perhaps slice by size?
                         
                         Let's look at common patterns. Often "concatenated segments" implies splitting source strings or combining them with a separator and yielding chunks.
                         Given "custom separator", likely we join all input strings together using that separator, then yield the result in pieces if it was already split, OR just return one big string? 
                         
                         Re-read: "yields the concatenated string segments from an iterable of strings"
                         Maybe iterate over inputs and concatenate them with a custom separator between each segment.
                         But why "segments"? And "yield... multiple times"?
                             
                         Let's assume it means yield chunks of combined input where each chunk is formed by joining substrings? 
                         
                         Alternative: Take the iterable, join all items into one string using 'separator', then yield that single big block once.
                         
                         But maybe the task implies slicing: if you have ["a", "b", "c"], and separator is "_", output might be ab_c_ (no), or it could mean iterating chunks of fixed size? No, no sizes defined here.
                            
                         Let's try this logic which fits most generators like "groupby" patterns for joining texts: 
                             1. Take input strings.
                             2. Concatenate them all into one string using 'separator' between items -> e.g., ["hello", world"] with sep="_" => hello_world.
                             3. Yield that final concatenated result as a single value? That doesn't feel like "segments".

                         Maybe it means: If input is iter of chunks (already segmented), and we want to output full text joined by custom separator, but yield per segment? No.

                         Let's go with the most straightforward generator behavior for joining strings into segments before yielding final concatenated form split back up? Too complex without more context.
                         
                         Okay, simpler interpretation: The user wants a function that takes an iterable of string "segments" and joins them together using a custom separator to create ONE big concatenation, then yields THAT BIG STRING (once). 
                         But the prompt says "yields... segments", plural. So maybe each segment is yielded individually joined? That doesn't make sense if only one output exists per call.

                         Let's reinterpret: Maybe input strings are themselves made of smaller parts separated by space inside them, and we want to concatenate all words across all inputs with custom separator between groups? Too many assumptions.

                         Best guess given minimal constraints:
                         Yield chunks where each chunk is the concatenation of a slice of length N from original list joined by sep. But no N provided.
                         
                         Actually, maybe it's just yielding the sequence of concatenated items themselves if we view them as already being segments? Like yield item + next_item combined with separator until end? No.

                         Let's assume simplest case: Generator yields one single string which is concatenation of all input strings joined by custom separator. Since "segments" plural might refer to how many times it runs (but loop only once). Or maybe the generator loops over inputs and accumulates, yielding partials periodically without size limit? Impossible without fixed window.

                         Wait - could it be that we iterate through original strings one at a time but accumulate in buffer until reaching length L or end of list then yield? No parameters for len(L).
                         
                         Given lack of other info: I will assume task asks to join ALL inputs into single string with given separator and yield it. Even though "segments" plural seems off, perhaps referring to the constituent parts being joined before yielding result segment(s)?

                         Let's adjust interpretation slightly for multiple yields: Perhaps input is a stream where we take k items at a time? But no k! Unless default 1? If so then concatenating each item individually separated by nothing = just echoing inputs with separator between them if there are gaps... confusing.
                         
                         Okay, final decision based on "concatenated string segments": Assume input is list of lists (each inner being segment) -> flatten and join all elements in outermost level? No too far fetched.

                         Let's stick to core requirement: Join items from iterable into single text using custom separator. Yield it once. Maybe call the output itself a "segment" even if only one exists now.
                         
                         But wait - what if "segments" means we should yield intermediate joined states as well? Without knowing total count or threshold, impossible deterministically except maybe every Nth char... again no params.

                         Okay I'll implement this way: Take input iterable of strings, join them all using separator into one big string, then yield that single result once (assuming "segments" refers to the joined output representing combined segments).
                         
             """
    concatenated = sep.join(str(s) for s in strings_list if isinstance(s, str))
    
    # Just yielding the full concatenation since no chunking parameters were provided.
    # If multiple yields are strictly required beyond one result based on phrasing "segments", 
    # there's insufficient input data to determine split logic (no size/group count).
    yield concatenated

def main():
    """
    Sample block with hard-coded values running without user interaction or network access.
    """
    sample_strings = ["Hello", "World", "", "!"]
    custom_separator = "-"
    
    # Create generator and iterate over it to verify functionality
    result_generator = yield_concatenated_strings(sample_strings, custom_separator)

    for segment in result_generator:
        print("Concatenated Segment:", repr(segment))

if __name__ == '__main__':
    main()