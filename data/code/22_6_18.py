def odd_even_generator(start: int = 1, end: int = None) -> str:
    """
    Generator function that yields a string indicating whether each number 
    in the range [start, end] is even or odd. 

    Args:
        start (int): The starting integer of the range (inclusive). Default is 1.
        end (int): The ending integer of the range (exclusive by Python's standard convention, inclusive if desired but here treated as upper bound exclusive for typical ranges like '1 to 20'). However, based on common phrasing "1 to 20" often implies [start, end] or [start, end-1]. Let's treat it as `range(start, end + 1)` if the user meant inclusive 1..20. To be safe and memory efficient without list creation:
        We will iterate using a loop that calculates parity on the fly.

    Yields:
        str: A formatted string "X is EVEN" or "X is ODD".
    
    Memory Efficiency:
        This function does not store any numbers in lists or dictionaries during iteration; 
        it yields results one by one, allowing infinite streams and constant memory usage relative to range size.
    """
    # If end is None, default to start + 20 for a short demo if needed later, but typically user sets both.
    # Let's assume inclusive range logic: if '1 to 20' means [1, 20], we go up to 20. 
    # Standard Python range is exclusive at the end. So if input is start and target_end (inclusive), add +1? 
    # Actually, let's stick to standard behavior where argument is just an upper bound logic or clarify:
    # "e.g., 1 to 20" usually means inclusive [1, 20]. I will handle end as exclusive by adding 1 if the intention was inclusive.
    # However, without explicit instruction on inclusivity of 'end', standard python range usage is start (inclusive) up to but not including end. 
    # Let's assume "1 to 20" means we want numbers 1 through 20 included. So effective_end = end if end else None + adjustment?
    # To keep it simple and robust: If `end` is provided, I'll treat the range as [start, end] inclusive -> iterate while n <= end.
    
    current_num = start
    
    def _is_even(n): return (n % 2 == 0)

    if end is None or isinstance(end, str): # Handle potential string conversion for safety in some edge cases but spec says integers implied by "1 to 20"
        pass 
    
    while True: 
         n = current_num
         status = "EVEN" if _is_even(n) else "ODD"
         yield f"{n} is {status}"
         
         # Logic for range termination needs clarification on 'end' parameter nature. 
         # If passed as int, usually implies upper bound limit.
         # Let's define a default stop condition inside or rely on caller? 
         # Generator should have a clear exit point if finite range requested without explicit count argument.
         # The prompt says "given range (e.g., 1 to 20)". This implies `start` and `end`.
         # I will implement so that it runs forever by default unless stopped, but provide an internal mechanism or simply loop until a specific condition? 
         # Actually generators are often used for infinite streams. But task asks "for every number in a given range".
         # So I need to define the `end` parameter behavior strictly.
         
         if isinstance(end, int):
            if n > end: break # Stop after exceeding inclusive limit 'end' (assuming user wants 1..20 -> stop at 21)

def main():
    """Main block with hard-coded sample values."""
    
    # Define the range directly as per "e.g., 1 to 20" which means inclusive [1, 20]
    start_val = 1 
    end_val_inclusive = 20
    
    print("Odd/Even Check Results (Sample: 1 to 20):")
    
    # Generate results and collect/print them. 
    # We could just iterate directly in the main block without storing in a list, maintaining memory efficiency.
    gen_obj = odd_even_generator(start=start_val, end=end_val_inclusive)
    
    for item in gen_obj:
        print(item + " ")

if __name__ == '__main__':
    main()