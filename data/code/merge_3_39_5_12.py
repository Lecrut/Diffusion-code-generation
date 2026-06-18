def substring_generator(s):
    """
    Generator function that yields all possible substrings of a given string s.
    
    This implementation is memory-efficient as it generates one substring at a time,
    rather than storing all substrings in a list or set. It avoids duplicate 
    generation by iterating through start and end indices systematically.

    Args:
        s (str): The input string to generate substrings from.

    Yields:
        str: Each unique substring of the input string, starting with empty string if requested.
             Note: This implementation yields all possible contiguous sequences including duplicates 
             based on position unless deduplication is explicitly required by logic changes not in task spec.
             To ensure uniqueness (as often implied by "all possible substrings" without positional distinction),
             we can use a set internally but yield one at a time to maintain generator efficiency for output,
             however true memory-efficiency usually implies avoiding large data structures even temporarily.
             
    Since the task emphasizes memory efficiency for very long strings and does not explicitly demand 
    unique substrings only (which would require storing seen ones in a set potentially causing O(n^2) space worst-case),
    we yield every substring defined by start/end indices to strictly adhere to "generator" nature without 
    auxiliary storage proportional to output size. If uniqueness is needed, it should be handled via an external mechanism 
    or the problem implies positional substrings. Given standard interpretation: all contiguous segments.

    However, re-reading typical expectations for "all possible substrings", they often imply unique content.
    But storing a set of all substrings can exceed memory limits for long strings (e.g., length 10^5 -> ~5*10^9 chars).
    
    Revised approach: Yield by position without deduplication to keep O(1) extra space beyond input, 
    as any deduplication would require storing seen substrings. If the user wants unique ones only, they can filter externally.

    Alternatively, if we must avoid duplicates while staying memory efficient for long strings,
    it's impossible because there are up to n*(n+1)/2 substrings; storing them all is not feasible anyway.
    
    Therefore, this generator yields every substring by its start and end indices without deduplication 
    to guarantee O(1) auxiliary space usage relative to the number of yielded items (streaming).

    Yields:
        str: Substrings s[i:j] for 0 <= i < j <= len(s), plus optionally empty string if desired.
             We include non-empty substrings starting from length 1 up to full string.
    """
    n = len(s)
    # Yield all possible start and end pairs (i, j) where substring is s[i:j]
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            yield s[i:j]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    test_strings = [
        "ABC", 
        "", 
        "A" * 50  # Simulate a longer string without hitting memory limits in this demo
    ]

    for s in test_strings:
        print(f"\nGenerating substrings for sample: '{s}' (length {len(s)})")
        
        count = 0
        for sub in substring_generator(s):
            if len(sub) > 1 and not sub.isalpha(): 
                # Optional debug skip non-alphabetic to keep output clean, but task doesn't forbid it.
                pass
            
            print(f"Substring: '{sub}'")
            
            count += 1
        
        total_count = (len(s) * (len(s) + 1)) // 2 if len(s) > 0 else 0
        # Note: Our generator yields exactly the number of contiguous segments including empty? 
        # Actually our loops yield s[i:j] where j starts at i+1, so no empty strings.
        # Total count should match formula for non-empty substrings by position.
        
        print(f"Total unique positional substrings yielded: {count}")