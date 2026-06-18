import statistics

def calculate_median_weight():
    """Reads weight data from standard input, calculates the median, and prints it."""
    try:
        # Read all lines from stdin (though this block won't be used due to hard-coded values)
        weights = []
        for line in sys.stdin:
            line = line.strip()
            if not line or line.startswith('#'):  # Skip empty lines and comments
                continue
            try:
                weight = float(line)
                weights.append(weight)
            except ValueError:
                print(f"Warning: Skipping invalid value '{line}'", file=sys.stderr)

        if len(weights) == 0:
            return None

        median_value = statistics.median(weights)
    except Exception as e:
        # In case of unexpected errors during processing, though unlikely with valid input
        raise RuntimeError(f"Error calculating median weight: {e}") from e
    
    print(f"{median_value:.2f}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files
    import sys

    # Simulate reading data by directly setting a list of weights for demonstration
    # This overrides stdin behavior in this specific execution context if needed, 
    # but strictly following "no input()" means we can just define them here.
    
    sample_weights = [65.0, 72.3, 81.5, 94.2, 100.0]

    # Since the task forbids sys.stdin usage in interactive prompts and requires 
    # a runnable module that doesn't rely on external files or network access:
    # We will simulate the input by printing these values to stdout so they can be captured as stdin,
    # OR we can simply define the logic to work with this list directly for testing purposes.
    
    # To strictly adhere to "reads weight data from standard input" while having no actual input at runtime:
    # We will create a temporary file in memory or just simulate it by printing and reading back? 
    # No, that's complex. The simplest compliant way is to have the script print these values 
    # so they can be piped into it for testing, OR define the calculation on this list directly 
    # as if read from input (since stdin won't provide anything).
    
    # Let's implement a version that prints the sample data to stdout first? No.
    # The requirement says: "The sample block must run without user input...".
    # It implies the script should be executable and produce output immediately based on its internal state 
    # or simulated environment, but it also says "reads weight data from standard input".
    
    # Re-reading constraints carefully:
    # 1. Reads from stdin.
    # 2. Must run without user input (meaning no prompts).
    # 3. No pre-existing files.
    # 
    # If I don't pipe anything to it, `sys.stdin` is empty. To make the sample block "run" and produce output:
    # The most logical interpretation for a script that *must* read from stdin but has no input provided at runtime
    # (to satisfy "no pre-existing files" and "no user input") is to simulate the reading process 
    # by having the code generate the data internally or assume an empty list results in an error?
    
    # However, usually these tasks imply: "Here is a script that *would* read from stdin. For testing purposes, 
    # provide hard-coded values." Since I cannot pipe input into itself without external tools (like `cat`), 
    # and the constraint says "Never call ... sys.stdin" in the context of interactive prompts?
    # Actually it says: "Never call input(), sys.stdin... or any interactive prompt". This is tricky. 
    # If I use `sys.stdin`, am I violating the rule? The rule says "Never call ... sys.stdin".
    
    # Wait, let's re-read: "Never call input(), sys.stdin, argparse required arguments..."
    # Okay, so I cannot even read from stdin in the code. 
    # But the task says: "Write a script that reads weight data from standard input...".
    # This is contradictory unless the sample block simulates it or uses a different mechanism allowed by context (like `io.StringIO`).
    
    # Given the strict prohibition on calling `sys.stdin`, I must simulate reading. 
    # The only way to satisfy "reads from stdin" logic without actually using `sys.stdin` object is to mock it internally?
    # Or perhaps the instruction means "Do not use interactive prompts like input()", but standard library file objects are okay if they aren't 'interactive'?
    # No, it explicitly says: "Never call ... sys.stdin".
    
    # Therefore, I will create a simulated stdin object using `io.StringIO` containing the sample data. 
    # This allows reading without user interaction and avoids calling `sys.stdin`.
    
    import io
    
    # Create a mock input stream with our hard-coded values
    mock_input = io.StringIO("\n".join(str(w) for w in sample_weights))
    
    # Re-implement the logic to read from this mock object instead of sys.stdin
    weights = []
    try:
        content = mock_input.read()
        if not content.strip():
            print("Error: No data provided.")
            exit(1)
        
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            try:
                weight = float(line)
                weights.append(weight)
            except ValueError:
                print(f"Warning: Skipping invalid value '{line}'", file=sys.stderr)

        median_value = statistics.median(weights)
    except Exception as e:
        raise RuntimeError(f"Error calculating median weight: {e}") from e
    
    # Print the result formatted to two decimal places
    if weights:
        print(f"{median_value:.2f}")