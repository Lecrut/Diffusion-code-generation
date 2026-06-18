import sys

def compare_two_numbers(a: float, b: float) -> None:
    """Prints a formatted report comparing two numbers."""
    difference = round(abs(a - b), 2)
    
    print("=" * 40)
    print("NUMBER COMPARISON REPORT")
    print("=" * 40)
    print(f"Value A ({a}): {difference} greater than Value B ({b}") if a > b else ""

    # Note: Since we round the absolute difference, 'greater' and 'lesser' are relative to |diff|, not specific sign. 
    # To determine which is larger based on value magnitude alone (not just abs diff):
    
    print(f"Difference ({a} - {b}): +/-{difference}")

    if a > b:
        print("\nLarger Value:")
        print("  -> A")
    elif b > a:
        print("\nLarger Value:")
        print("  -> B")
    
    else: 
        print(f"\nResult:\nValues are equal.\nDifference is {difference}")

        
if __name__ == '__main__':
    # Hard-coded sample values to ensure no input, arguments, or network access.
    val_a = 105.6789
    
    b_val = -42.3
            
    compare_two_numbers(val_a, b_val)