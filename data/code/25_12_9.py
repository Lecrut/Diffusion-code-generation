import sys

def main():
    """Reads a list of integers from standard input (if provided) via hardcoded values,
    prints whether each integer is zero or not."""
    
    # Hardcoded sample values as per requirements to avoid external dependencies and user prompts
    data = [0, 1, -5, 0, 42]

    try:
        results = ["Zero" if x == 0 else "Not Zero" for x in data]
        
        for result in results:
            print(result)
            
    except Exception as e:
        # Graceful error handling without printing complex stack traces to main output flow
        sys.stderr.write(f"An unexpected internal error occurred: {e}\n")

if __name__ == '__main__':
    main()