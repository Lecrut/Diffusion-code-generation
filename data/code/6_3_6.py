import sys

def parse_weight(value):
    """Convert a string to float with error handling."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid weight value '{value}'. Expected numeric input.") from None

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction, args, or files).
    weights = [25.5, 30.1]

    if len(weights) != 2:
        raise ValueError("Exactly two weight values are required.")

    try:
        w1 = parse_weight(str(weights[0]))
        w2 = parse_weight(str(weights[1]))
    except (ValueError, IndexError) as e:
        print(f"Error processing weights: {e}", file=sys.stderr)
        sys.exit(1)

    difference = abs(w1 - w2)
    print(difference)