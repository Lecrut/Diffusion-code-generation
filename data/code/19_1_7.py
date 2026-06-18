def is_greater(a: int | float) -> bool:
    """Returns True if a > b, where a is passed as argument."""
    
def main():
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    result1 = is_greater(5.0, 3.0)
    print(result1)

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            result = is_greater(a, b)
            print(result)
        except ValueError as e:
            print(f"Error converting input to numbers: {e}", file=sys.stderr)
    else:
        main()