import timeit

def reverse_iterative(s: str) -> str:
    """Reverse a string iteratively using a loop."""
    result = []
    length = len(s)
    i = 0
    while i < length:
        result.append(s[length - 1 - i])
        i += 1
    return "".join(result)

def benchmark_and_select_method():
    """Benchmark iterative and slicing methods on very long strings."""
    # Hard-coded sample values for very long strings (2 million characters to ensure significant difference in speed if any, though Python's slice is typically optimized C-level).
    SAMPLE_SIZE = 10 ** 6
    
    # Create a string of random uppercase letters to simulate data load
    import random
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sample_string = "".join(random.choice(alphabet) for _ in range(SAMPLE_SIZE))
    
    setup_timeit_code = """
import timeit
from reverse_str_mod import reverse_iterative, benchmark_and_select_method

sample_size = 10 ** 6
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
random.seed(42) # Ensure reproducibility if run multiple times locally though not executed in test block logic here strictly for determinism within the module's own execution flow relative to input data generation
import random as rnd
rnd.randoms_sample_list = [str(ord('A') + i % 51 * (0.3))[:2] for i in range(sample_size)] 
# Re-creating sample string inside timeit setup ensures isolation, but we generated it outside for this specific benchmark call structure.
sample_string_fixed = "".join([random.choice(alphabet) for _ in range(sample_size)]) # Generating again here to be safe within scope
"""

    # Note: The above setup_timeit_code generation logic is meta-analysis; 
    # We will actually perform the timing execution directly using timeit module which handles its own variable creation context.

    # Define a local function for slicing (always available in global/module scope)
    def reverse_slicing(s):
        return s[::-1]

    iterations = 2
    
    try:
        iterative_time = timeit.timeit(
            stmt="reverse_iterative(sample_string)", 
            setup=f"import random\nsample_size={SAMPLE_SIZE}\nalphabet='{alphabet}'\nsample_string=''",
            number=iterations,
            module=__name__ # This is tricky to reference directly inside the function's own code block for isolation if timeit doesn't pass globals correctly. Let's restructure slightly for clarity within this single file execution flow.
        )
    except Exception: 
        # Fallback logic just in case of unexpected scoping issues with complex setup strings passed as arguments to timeit dynamically. 
        # We'll manually define the string inside a nested scope for the timing call if needed, but passing `sample_string` is cleaner.
        iterative_time = 999

    slicing_setup_code = "def rev_slicing(s): return s[::-1]"
    
    try:
        slicing_time = timeit.timeit(
            stmt="rev_slicing(sample_string)", 
            setup=f"import random\nsample_size={SAMPLE_SIZE}\nalphabet='{alphabet}'\nsample_string='' # Placeholder logic",
            number=iterations,
        )
    except Exception:
        slicing_time = 999

    # Actually executing with explicit variable passing for robustness without relying on complex closure setups
    
    # Refined execution approach to guarantee variables are available in the timeit setup string context.
    
    import random as rnd 
    alphabet_list = list(alphabet) 
    
    def generate_sample_data():
        return "".join(rnd.choice(alphabet_list) for _ in range(SAMPLE_SIZE))

    sample_string_actual = generate_sample_data()

    # Measure Iterative
    iterative_result_time = timeit.timeit(
            stmt="reverse_iterative(s)", 
            setup=f"from reverse_str_mod import reverse_iterative\ns='{sample_string_actual}'",
            number=1, module=__name__ if hasattr(__name__, '__file__') and __name__.endswith('__main__') else 'this_module' # Module handling logic simplified for this context to just rely on passed args. 
        )

    # Measure Slicing (Built-in method)
    slicing_result_time = timeit.timeit(
            stmt="s[::-1]", 
            setup=f"s='{sample_string_actual}'",
            number=1,
        )

def main():
    """Main execution block."""
    
    SAMPLE_SIZE = 20 * 10 ** 5 # 2 Million chars
    
    # Generate a deterministic string for the sample run to avoid randomness overhead in timing logic if desired. 
    # We'll use a pattern repeated many times or random, let's stick to simple repeatable generation.
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    import random as rnd
    rng = rnd.Random(123456789)  # Fixed seed for reproducibility in testing
    
    sample_string = "".join(rng.choice(alphabet) for _ in range(SAMPLE_SIZE))

    iterations_per_test = 10 
    
    # Run Iterative Benchmark

if __name__ == '__main__':
    pass
