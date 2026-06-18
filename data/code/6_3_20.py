import sys

def parse_weight(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid weight value: '{value}'")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed)
    val1 = "75.5"
    val2 = "80.3"

    try:
        w1 = parse_weight(val1)
        w2 = parse_weight(val2)
        difference = w1 - w2
        print(difference)
    except ValueError as e:
        # Handle the specific error from our parser or any other unexpected exception
        if "Invalid weight value" in str(e):
            sys.stderr.write(f"Error: {e}\n")
        else:
            raise