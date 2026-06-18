import sys

def find_matching_pairs(values_list):
    """
    Generator function that yields True whenever two values from 
    the input list match each other (i.e., value at index i equals value at index j, where i != j).
    
    Args:
        values_list (list): List of potential pairs/values to compare.
        
    Yields:
        bool: True if a matching pair is found, False otherwise within the current iteration context 
             based on problem statement interpretation for 'match'. However, re-reading "yields `True` only when two provided values are found to be a match" suggests we yield once per unique matching pair or continuously?
             
    Clarification of logic: The prompt says "iterating over a list of potential pairs". 
    If the input is just one flat list [a, b, c], finding matches means checking if any element repeats.
    But it also says "two provided values are found to be a match", implying we might receive pairs or check indices.
    
    Let's assume standard behavior: Iterate through all combinations of two items in the input list and yield True 
    immediately upon discovering that item[i] == item[j]. Note: A generator yielding 'True' repeatedly is unusual for "only when". 
    To strictly follow "yields True only when... found to be a match", if we find one, do we exit? No, generators continue unless stopped.
    
    Refined Interpretation: The prompt likely implies checking distinct indices i and j where values[i] == values[j].
    We will yield 'True' every time such a pair is identified. If no pairs exist in a specific check cycle (though here it's one full pass), we don't explicitly yield False unless requested, 
    but the requirement "yields True only when" implies that on non-matches, nothing should be yielded to avoid confusion, or perhaps implicit None/False behavior isn't needed if strictly yielding matches.
    
    However, looking at typical coding challenge patterns for this specific wording:
    Often it means checking pairs (a,b) from the list and returning a result set? No, "yields".
    
    Let's implement strict logic: 
    Iterate through all unique pairs of indices (i, j). If values[i] == values[j], yield True. Otherwise do nothing (since we only yield on match).
    This satisfies "yields True ONLY when two provided values are found to be a match". On non-matches, it yields nothing for that specific pair comparison logic within the generation flow? 
    Wait, generators run until exhausted. If I don't yield anything in one iteration block but do in another...
    
    Actually, simpler interpretation: Check if there exists ANY matching pair. But since it's a generator over "potential pairs", let's assume we process every possible combination of two items from the list and output status? 
    No, "yields True only when". This usually means: Iterate through combinations -> If match -> Yield True; Else -> (Do not yield).
    
    Let's create sample data to test. Sample 1: [1, 2, 3] -> No matches -> Yields nothing. 
    Sample 2: [1, 2, 1] -> Match found at indices 0 and 2 -> Yield True once (or multiple times depending on pair definition).
    
    Let's define "two provided values" as taking two items from the list one by one? Or a flat list where we check duplicates.
    Given "iterating over a list of potential pairs", maybe the input IS a list of tuples/pairs, and we check if p1 == p2? 
    But it says "two provided values are found to be a match". Singular/Plural ambiguity.
    
    Safe bet: Input is `values_list`. We generate all unique combinations `(a, b)` with indices different. If equal, yield True.
    
    """
    n = len(values_list)
    # Generate pairs of distinct indices
    for i in range(n):
        for j in range(i + 1, n):
            if values_list[i] == values_list[j]:
                yield True

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input, args, network)
    
    # Sample Case 1: List with duplicates to trigger a match
    data_with_matches = [5, 3, 8, 5] 
    print("--- Testing list with matches ---")
    count_match_case_1 = sum(1 for _ in find_matching_pairs(data_with_matches))
    
    # Sample Case 2: List without duplicates to verify no True is yielded (generator yields nothing)
    data_no_matches = [4, 9, 7] 
    print("--- Testing list without matches ---")
    count_match_case_2 = sum(1 for _ in find_matching_pairs(data_no_matches))

    # Sample Case 3: List with multiple duplicate types or one type appearing thrice
    data_multiple_dupes = [10, 20, 10, 30] 
    print("--- Testing list with multiple matching pairs ---")
    count_match_case_3 = sum(1 for _ in find_matching_pairs(data_multiple_dupes))

    # Display results to confirm logic (though output format not strictly defined beyond runnable module)
    if data_with_matches: print(f"Match found in Case 1, yield count: {count_match_case_1}")
    else:     print("No matches found in Case 1")