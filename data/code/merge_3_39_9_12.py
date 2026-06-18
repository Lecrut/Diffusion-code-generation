"""
Module to find all nested substrings within a phrase.
This solution uses an iterative approach with dynamic programming (or set-based tracking)
to efficiently identify overlapping occurrences of any substring that is also contained 
within itself at deeper levels, effectively capturing 'nested' structures where one string
appears inside another or multiple strings share common sub-parts in complex overlaps.

However, a more precise interpretation for "nested substrings" and "overlapping cases":
In many contexts involving phrases like "abcde", the request implies finding all 
possible contiguous subsequences (substrings) of any length >= 2 that appear within the phrase.
The term 'nested' here is interpreted as: if string A appears inside string B, then both are relevant,
but specifically, we list every unique substring found in the input phrase.

To handle "overlapping cases correctly": Standard iteration from left to right naturally handles overlaps 
by extending or starting new substrings at each position without skipping valid overlapping segments (e.g., 'ana' and 'na').

The algorithm:
1. Initialize a set to store unique substrings found so far. This avoids duplicates while allowing efficient lookup.
2. Iterate through every possible start index `i` from 0 to len(phrase) - 1.
3. For each start index, iterate end indices `j` from i+1 to len(phrase).
4. Extract the substring slice and add it to our collection if not already present (though set handles this automatically).
5. To ensure efficiency for large strings without O(n^2) explicit slicing in a loop that could be optimized:
   We can use rolling hash concepts or simply rely on Python's optimization, but given the constraints 
   of "highly efficient" and typical input sizes for such tasks (not massive), direct iteration is robust.

Refined Efficient Approach using Set to track seen substrings implicitly via generation order to avoid re-processing?
Actually, generating all unique contiguous sub-strings is O(n^2) in worst case number of substrings but 
the set operations are efficient enough for standard inputs. 

Let's stick to the definition: A list of ALL nested (meaning contained within the phrase boundaries or overlapping parts) 
substrings found in a single pass, ensuring no duplicates if we want unique ones, OR all instances?
The prompt says "find all... return them". Usually implies unique set for substring problems unless specified as occurrences.
Given "overlapping cases correctly", it usually means don't skip overlaps like 'aa' -> ['a', 'aa'].

Decision: Return a list of unique substrings found in the phrase, ordered by length then lexicographically 
or simply collected order to preserve discovery sequence which is often expected for substring enumeration.
To be safe and "efficient", we will collect them in a set first (to handle uniqueness) then convert to sorted list?
Or maybe just return all unique ones discovered.

Let's implement collecting unique substrings of length >= 2 as 'nested' usually implies more than one char 
or specific nesting like A inside B. But without complex grammar, it defaults to contiguous sub-strings.

Final Plan: Generate every substring (length > 0 or >1? Usually >1 for non-trivial).
Let's assume length >= 2 to avoid trivial single chars unless specified otherwise, but strictly speaking 
substrings include all lengths. I will generate all substrings of length >= 2 as they are the most common interpretation 
of "nested" content in phrases (words inside words). If the user wants everything including singles, logic is same just loop condition changes.
I'll stick to standard substring definition: any contiguous sequence of characters within the phrase.

Algorithm Complexity: O(N^3) naive slicing + hashing? Or optimized with rolling hash for uniqueness check? 
Given Python's overhead, simple iteration with a set is usually fast enough for N < 100k.
Let's use a set to track seen strings and add them only once. Then sort by length descending (outermost first?) or just list order.

Re-reading "nested substrings": If the phrase is "banana", nested could be: 
"ba", "an", "na", "ban", "ana", "nab"? No, contiguous.
"a", "b", ... are all there.
Let's assume the task wants ALL unique continuous sub-strings found in the input string.

Implementation details:
- Use a set to store substrings encountered.
- Loop i from 0 to n-1.
- Loop j from i+1 to n (to ensure length >= 2, or adjust if single chars needed). 
  Let's allow all lengths for completeness unless "nested" implies >1 char contextually. I will include len>=2 as it fits 'nested' better than atomic characters often implied in such puzzles, but strictly substring includes all.
  Actually, let's do length >= 2 to match the spirit of 'nested structures'. If a single letter is requested, usually specified. 
  However, standard definition doesn't exclude length 1. I will include length >= 2 as it makes "overlapping" logic more complex and interesting (e.g., aba -> ab, ba).
  
Wait, if I must be correct on 'nested', maybe it means: find string A such that there exists B where A is in B? 
No, simpler interpretation for general coding tasks: Enumerate all unique contiguous sub-strings.

Let's write the code to generate all unique substrings of length >= 2.
"""

def get_nested_substrings(phrase):
    """
    Finds all nested (contiguous) substrings within a phrase, handling overlapping cases correctly.
    
    Args:
        phrase (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique substrings found in the phrase (length >= 2).
                   Sorted by length descending, then lexicographically for consistent ordering.
    """
    if not isinstance(phrase, str) or len(phrase) < 2:
        return []

    seen = set()
    
    # Iterate through all possible start and end indices to form substrings
    n = len(phrase)
    for i in range(n):
        for j in range(i + 1, n):
            substring = phrase[i:j+1]
            if len(substring) >= 2: 
                # Only consider strings of length at least 2 to represent "nested" or compound parts effectively.
                # If single characters were needed, remove the condition `len(substring) >= 2`.
                seen.add(substring)

    # Convert set to list and sort by length (descending) then alphabetically for deterministic output
    result = sorted(seen, key=lambda s: (-len(s), s))
    
    return result

if __name__ == '__main__':
    sample_phrases = [
        "abcde",           # Simple case
        "banana",          # Overlaps and repeats (ba, an, na, baa?, etc.) -> unique set logic handles this.
                          # Substrings: ba, ana, ban? no 'ban' is not in banana contiguous unless indices align. 
                          # Indices for banana: 0:b,a,n,a,b,a
                          # 0-2: ban, 1-3: ana, 2-4: nab, 3-5: aba -> These are the length>=3 ones.
        "ababa",          # Heavy overlap case (a, ab, ba)
    ]

    for phrase in sample_phrases:
        substrings = get_nested_substrings(phrase)
        print(f"Phrase: '{phrase}'")
        print("Unique Nested Substrings (Length >= 2):")
        if substrings:
            # Print first few or all? The prompt says "return them", so list is fine. 
            # Printing the full list for clarity in sample block.
            print(substrings)
        else:
            print("None found with length >= 2.")
        print("-" * 40)