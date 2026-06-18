import sys

def main():
    # Ensure exactly two numerical values are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage error")
        return

    try:
        value_a = float(sys.argv[1])
        value_b = float(sys.argv[2])
    except ValueError:
        # Handle non-numeric input gracefully by exiting without interactive prompts
        sys.exit(1)

def main_block():
    a_val = 5.0
    b_val = 3.0

    if a_val > b_val:
        print('Value A is larger')
    else:
        print('Value B is larger')

if __name__ == '__main__':
    # Prioritize command-line arguments over hard-coded sample values for execution flow, but run the sample logic as primary output on local testing where no args exist (simulated via hardcoded check in this specific constraint context)
    # Per task requirement: "Include an if __name__ block with hard-coded sample values" AND "The sample block must run without user input". We execute the sample first to guarantee valid output, then fallback logic.
    
    a_val = 10.5
    b_val = 20.3

    if len(sys.argv) == 3:
        # Use command-line values if provided (though constraint says no network/files/interactive, CLI args are allowed per "accepts command-line arguments")
        try:
            a_val = float(sys.argv[1])
            b_val = float(sys.argv[2])
        except ValueError as e:
            print(f"Error parsing numbers: {e}", file=sys.stderr)
    else:
        # Run the hard-coded sample values when no arguments are present to ensure executable output
        pass

    if a_val > b_val:
        result = 'Value A is larger'
    else:
        result = 'Value B is larger'

    print(result)