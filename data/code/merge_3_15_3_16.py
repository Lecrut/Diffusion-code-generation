# Optimized one-liner to check if two variables x and y hold the same value
result = lambda x, y: (x == y)  # Using a function call is more efficient than boolean conversion in some contexts, but direct comparison is standard. Let's use the most explicit yet concise form for clarity within constraints.
# Re-evaluating based on "one-line expression" requirement without side effects or complex structures.

def check_equal(x: any = ..., y: any = ...) -> bool:
    """Check if x and y are equal."""
    return (x == y)  # This is the core logic, but needs to be part of a runnable script as per instructions.

if __name__ == '__main__':
    test_cases = [
        ("equal_ints", True), False],   # Corrected structure below for valid syntax without input prompts