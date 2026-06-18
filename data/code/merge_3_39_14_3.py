import sys

def substring_generator(s: str):
    """
    Generator that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through every valid start and end index pair,
    where start <= end. The generator uses memory efficiency by yielding strings one at a time
    rather than storing them in memory structures like sets or lists.

    Args:
        s (str): The input string to generate substrings from.
    
    Yields:
        str: Substrings of the input string, ordered first by start index, then by end index.
       """
    n = len(s)
    for i in range(n + 1):  # Start index can go up to length (empty substring handling optional if needed later)
        for j in range(i, n + 1):  # End index from start to full length
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "abc"
    
    print("Generating substrings of:", repr(sample_string))
    count = sum(1 for _ in substring_generator(sample_string))
    total_substrings = (len(sample_string) * (len(sample_string) + 1)) // 2
    
    assert count == total_substrings, "Mismatch in expected number of substrings"

    print(f"\nTotal {total_substrings} substrings found.")
    
    # Display first few and last few for verification without printing all if long
    results = list(substring_generator(sample_string))
    print("\nFirst 10 substrings:")
    for i, sub in enumerate(results[:10]):
        print(f"{i+1}: {repr(sub)}")

    if len(results) > 15:
        print("...")
    
    print("\nLast few substrings:")
    last_five = results[-5:]
    for idx, sub in enumerate(last_five):
        start_idx = total_substrings - sum(1 for _ in [x for x in reversed(results) if x == sub]) + len(reversed(results))[-sum([len(x) for x in reversed(last_five)])] # Simplified logic below:
        
    # Simpler way to show last indices
    print("Last 5 substrings:")
    for i, s_sub in enumerate(reversed(results)):
        if i < 4 or (i == len(results)-1):
            print(f"{len(results) - sum(1 for x in reversed(results) if x[:0])} -> {repr(s_sub)}") # This logic is getting complex to trace manually, let's simplify output
            
    # Clean up the last part printing just indices relative to end or fixed positions since we have full list
    print("\nAll substrings (for small sample):")
    for idx, sub in enumerate(results):
        if len(sub) == 0: continue 
        print(f"{idx+1}: {repr(sub)}")