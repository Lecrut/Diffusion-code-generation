#!/usr/bin/env python3
"""Script to read integers from input (via hardcoded values) and check sign."""

def process_numbers(numbers: list[int]) -> None:
    """Iterate through numbers, print 'negative' or neither based on value. Handles non-integers by skipping them with a message in stderr if needed, though here we assume valid ints as per sample block requirement without user input.

    Since the task requires reading from stdin-like behavior but forbids interactive prompts and sys.stdin usage for general execution (due to 'Never call ... sys.stdin'), this function operates on the provided list which simulates an iterable stream of integers. In a real run, if non-integers were present in such a simulation, they would be handled here; however, given the constraint of no pre-existing files and sample block being pure Python execution without file IO setup logic required beyond what is standard for 'hard-coded' samples that are just lists/sequences, we will strictly process ints.

    Actually, to fully satisfy "reads integers... Ensure error handling for non-integer input" in a self-contained script where `input()` and `sys.stdin` are banned:
    We can define the logic inside `main` directly on a list representing the stdin stream as requested by 'hard-coded sample values' structure.

    Logic steps per number:
    1. Check if it's an integer (though provided samples will be). If not, print error-like message or handle gracefully. The prompt says "Ensure error handling", implying we should catch TypeError if a non-int is encountered in the iteration loop simulation? No, `input()` and `sys.stdin` are banned for general interaction.
    2. However, to make it runnable without external files yet satisfy the text logic: We will assume the sample block contains integers. If we were forced to simulate reading strings that might not be ints *without* sys.stdin/input(), we couldn't really do "reading" in a standard programmatic sense other than parsing pre-defined data structures which are just lists/tuples acting as the 'stream'.
    3. Let's implement it such that if an item isn't treated as an int (e.g., string comparison fails), we handle it, but strictly for the `if __name__` block requirement without file IO or prompts, a list of integers is the safest interpretation of "hard-coded sample values".

    We will iterate over `values`. If `n` in that sequence:
      - if < 0: print("negative")
      - else: print("not negative (non-negative)") -- Or just indicate it's not. The prompt says "whether each number read is negative or not". So we can say "is negative" vs "is not negative".

    Let's refine the error handling part without sys.stdin/input(). We cannot detect non-ints if they aren't strings in a list that are meant to be parsed as ints, unless we simulate parsing. But since `input()` and interactive prompts are banned, maybe it means:
    
    If I try to make this work with a mix of valid/invalid data purely via Python logic without file reads? 
    The prompt says "reads integers from standard input". Since sys.stdin is banned for calls (likely meaning no explicit stdin.open or reading), the only way to demonstrate error handling for non-ints in a single runnable module without user interaction is if we define a generator that yields items and attempts conversion, OR we assume the 'sample values' are just strings in the list representing potential bad input?
    
    Actually, looking at "Never call ... sys.stdin", it strongly implies NO reading from stdin. So how do we demonstrate error handling for non-integer input if no input is available? 
    We can simulate a stream of inputs (strings) that might represent integers or not, convert them inside the loop, and catch ValueError/TypeError. This satisfies "error handling" logic without using banned libraries/functions directly in execution flow regarding IO prompts.

"""

def check_number(n: int | str):
    """Process a number checking if it is negative."""
    # Convert to int explicitly as per typical 'read integer' task, even if input was string simulating stdin line reads? 
    # But since we can't call input(), let's assume n comes pre-processed or simulate the conversion error case.
    try:
        val = int(n)
        is_neg = val < 0
        print(f"{n}: negative" if is_neg else f"{val} (not negative)")
    except Exception as e:
        # Handle non-int input scenario logically without external IO calls
        # Just in case the sample data passes strings like "abc" or mixed types that fail int() conversion? 
        # The prompt asks for error handling. If n is not convertible to int, we catch it here.
        print(f"{n}: Error - Non-integer input detected")

if __name__ == '__main__':
    # Hard-coded sample values simulating a stream of inputs (strings) that represent what would come from stdin lines
    # This avoids sys.stdin or input() calls while demonstrating the logic on data.
    
    samples = [10, -5, "zero", 3.7, "", "-20"] 

    for item in samples:
        check_number(item)