"""
Generator function to yield comparison results of two sequence lengths.
Optimized for memory efficiency by yielding a single boolean per iteration,
avoiding storage of all comparisons in memory for large sequences.
"""

def length_compare_generator(seq1_length: int, seq2_length: int):
    """
    Yields True if the first sequence is longer than the second, False otherwise.

    Args:
        seq1_length (int): Length of the first input sequence.
        seq2_length (int): Length of the second input sequence.

    Returns:
        Generator[bool]: A generator yielding boolean values representing the comparison result.
                         Since the lengths are static, this will yield a single value repeatedly 
                         or once depending on implementation choice for 'large sequences' simulation.
    
    Note:
        For true optimization in scenarios where we need to simulate iterating over many logical steps 
        without holding state outside of generators (e.g., if comparing cumulative progress), 
        one might iterate N times yielding the same result, but strictly speaking, a comparison 
        of two static lengths yields a constant. To fulfill the 'large sequences' requirement in terms 
        of potential use cases where length changes or steps are involved without memory bloat,
        this generator is structured to yield indefinitely with optional step-based logic if extended,
        but for direct length comparison, it yields once (or can be configured).

        *Correction based on strict task: "generates result of comparing two input lengths".*
        The result of a static comparison is constant. To make this useful as a generator 
        demonstrating memory efficiency over time/simulation steps without storing the list of results:
        
        We will yield the boolean value in an iterative manner (e.g., for N iterations) where N can be very large,
        ensuring no list or array of comparisons is ever created. This simulates processing streams 
        of items based on these lengths efficiently. If only a single comparison result is physically needed,
        it will yield once and stop if not asked to continue (though Python generators usually require an iterator protocol).
        
        However, the most logical interpretation for "comparing two input lengths" as a generator that handles 
        "very large sequences of comparisons" implies we are simulating a scenario where these lengths act as boundaries 
        over many steps. 

        Given the static inputs seq1_length and seq2_length:
        - If the task implies comparing them once, it's trivial.
        - If it implies generating a sequence of *potential* comparison results (e.g., for every item in a virtual stream),
          we can yield based on an index relative to these lengths or just repeat until exhaustion if treated as iterators over themselves?

        Let's assume the most robust interpretation: The user wants a generator that produces a result. 
        Since comparing two static numbers is constant, let's wrap it such that it yields the result once, 
        OR (to satisfy 'large sequences of comparisons') we can simulate processing up to `max(seq1_length, seq2_length)` steps?
        
        Actually, re-reading: "yields the result of comparing". This implies a sequence of results. 
        Since lengths are fixed, the comparison is constant unless there's an implicit index progression not mentioned.
        
        Let's assume a simple case where we just yield the boolean once to be precise about static inputs, 
        BUT if the prompt implies simulating comparisons across iterations (e.g., item i vs length), that would require more args.
        
        Alternative: Perhaps it means comparing cumulative lengths? No, explicit "two input lengths".

        Decision: The result of comparing two numbers is a single boolean. Generating this infinitely or repeatedly 
        without state changes isn't meaningful unless the inputs change dynamically (which they don't here). 
        To adhere to "large sequences", we will structure it such that if called in a context where many comparisons are needed,
        it yields efficiently. However, strictly speaking, comparing `10` and `5` is always True/False.

        Let's reinterpret: Maybe the inputs represent lengths of *streams* being compared item by item? 
        If so, we don't have access to the items, just their counts.
        
        To be safe and useful as a "generator", I will yield the result for each step `i` from 0 up to some limit derived from max length, 
        or simply yield once if that's all there is? No, a generator must support iteration.

        Let's assume the task implies: For a hypothetical stream of N comparisons (where N is huge), how do we generate results without storing them?
        Since our inputs are just two integers L1 and L2, the result A > B never changes.
        
        I will implement it to yield the boolean value repeatedly for `max(L1, L2) + 1` iterations (simulating a sequence of checks up to max length), 
        ensuring memory efficiency by not storing the list, just yielding one at a time. If N is larger than that, we stop or extend?
        
        Actually, simplest valid generator: Yield the result once. But "sequence of comparisons" suggests multiple yields.
        Let's assume the user might want to compare `index` against lengths in some loop but didn't specify index logic. 
        Without explicit index logic (e.g., comparing current_index with len1 vs len2), I cannot invent variables.

        Refined Plan: The function takes L1 and L2. It yields True if L1 > L2, else False.
        To satisfy "sequence of comparisons", perhaps the intention is to yield this result `max(L1, L2)` times? 
        Or maybe just 1 time? A generator that stops after one value is trivial but valid.
        
        However, let's look at the constraint: "optimized for memory efficiency when dealing with very large sequences of comparisons".
        This implies there ARE many comparisons to be performed/generated. Since L1 and L2 are static scalars in this function signature, 
        the only way to have a sequence is if we iterate through an index range implied by these lengths or arbitrary N?
        
        Let's assume the generator yields the comparison result for `max(L1, L2)` iterations (simulating checking up to max length).
        This demonstrates the ability to handle large iteration counts without memory overhead.

    """
    
    # Determine if seq1 is strictly longer than seq2
    result_value = True if seq1_length > seq2_length else False
    
    # Yield indefinitely or for a count? 
    # To satisfy "large sequences", let's yield 'result_value' repeatedly until we pass the max length,
    # effectively simulating N comparisons where N ~ max(L1, L2).
    # This avoids creating an array of booleans.
    
    limit = max(seq1_length, seq2_length) + 1
    
    for _ in range(limit):
        yield result_value

if __name__ == '__main__':
    # Hard-coded sample values representing lengths of two large virtual sequences
    length_a = 50_000_000   # Simulating a very long sequence A
    length_b = 123_456      # Simulating a much smaller sequence B

    print(f"Comparing sequence of length {length_a} vs {length_b}")
    
    # Demonstrate memory efficiency: iterate through the generator without storing it in a list
    comparison_results_count = sum(1 for _ in (i for i, val in enumerate(length_compare_generator(length_a, length_b)) if True)) 
    # The above line is just to show consumption. Let's do explicit iteration count logic differently to be clear.

    print("Generating comparisons...")
    
    # Count how many items are yielded before stopping naturally (based on max length)
    total_generated = 0
    for i, is_longer in enumerate(length_compare_generator(length_a, length_b)):
        if i == 1_000:
            break # Break early to keep sample output short without running 50M iterations here
        
        # In a real scenario with no stop flag logic inside generator (unless we use count), 
        # the loop would run max_len times. We broke at 1000 for demo speed.
        
    print(f"Comparison result: {length_a > length_b} ({'True' if is_longer else 'False'} in this instance)")