def find_matching_pairs(list_a, list_b):
    """
    Generator function that yields `True` if elements from two lists match at the same index,
    otherwise it implicitly does nothing (since we only care about matches). 
    However, to satisfy "yielding True ONLY when... found", we yield False for non-matches as per the prompt's implication of iterating over all pairs or just yielding on success?

    Re-reading: "yields `True` only when two provided values are found to be a match".
    This implies if they don't match, do not yield. 
    BUT then it says "iterating over a list of potential pairs".
    
    Let's interpret strictly: If index i matches, yield True. Else, skip (do nothing).
    Wait, usually such tasks imply yielding the pair status or just marking success.
    Given "yields `True` only when...", non-matches result in no yield from that step.

    However, a safer interpretation for debugging/usage is to iterate and print/yield results of comparison 
    but specifically ensure True comes out on match. Let's stick to the strict reading: Yield True if equal. 
    
    Actually, looking at standard generator patterns for this description often implies iterating through indices.
    
    Revised Logic: Iterate zipped lists. If elements are equal, yield True (and perhaps False? No "only when... found"). 
    So only yields on success.

    Wait, the prompt says "yields `True` ONLY WHEN...". It does NOT say it must yield anything else or skip otherwise explicitly to be silent.
    But typically users expect a sequence of booleans [T, F, T]. If we only yield True, they can't index non-matches easily.
    
    Let's re-read carefully: "yields `True` only when two provided values are found to be a match".
    This strongly suggests conditional yielding (if equal -> yield True; else -> do nothing). 
    Or does it mean "Return the result as True if match, False otherwise"?
    The word "only" is key. It restricts the positive outcome count.
    
    Let's assume the user wants an iterator that signals a hit. If they wanted all comparisons, they would say "yields a boolean for each pair". 
    I will implement it to yield `True` on match and nothing (or perhaps implicit False) otherwise? 
    Actually, looking at the phrase "iterating over a list of potential pairs", maybe the input is already a list of pairs?
    
    Scenario A: Input = [list1], find intersection. Loop indices. Match -> Yield True. Else ignore.
    Scenario B: Input = [(a,b), (c,d)...]. Iterate tuples. If equal, yield True.

    Let's assume the input is two separate lists to be compared element-wise as "pairs" formed by index.
    
    Implementation: 
    For a, b in zip(list_a, list_b):
        if a == b:
            yield True
    
    This satisfies "yields `True` only when...".

"""

def find_matching_pairs(list_a, list_b):
    """
    Yields `True` for any pair of values from two lists that are identical.
    Does not yield anything for non-matching pairs to strictly adhere to 
    'yields True ONLY WHEN ... match'.
    
    Args:
        list_a (list): First list of values.
        list_b (list): Second list of values.
        
    Yields:
        bool: True if elements at the same index are equal.
    """
    for item1, item2 in zip(list_a, list_b):
        if item1 == item2:
            yield True

if __name__ == '__main__':
    # Sample data provided directly without user input or files.
    
    sample_list_1 = [5, 3, 8, 'apple', None]
    sample_list_2 = [9, 3, 7, 'banana', None]

    print("Comparing the following pairs:")
    for is_match in find_matching_pairs(sample_list_1, sample_list_2):
        # Note: Only True will be yielded and printed here. 
        # If we wanted to know which index failed, a boolean list would be needed, 
        # but per strict instruction "yields True only when...":
        if is_match:
            print(f"Match found!")

    # Optional check for count of matches
    match_count = sum(1 for _ in find_matching_pairs(sample_list_1, sample_list_2))
    total_elements = len(sample_list_1)
    
    print(f"\nTotal elements checked (up to shortest list): {total_elements}")
    print(f"Number of matching pairs found: {match_count}")