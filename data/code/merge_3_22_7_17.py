import math

def get_remainder_and_parity(n: int) -> tuple[int, str]:
    """
    Returns a tuple containing (remainder_on_division_by_2, parity_description).
    
    Parameters:
        n (int): The integer input.
        
    Returns:
        tuple[int, str]: A tuple where the first element is n % 2 
                         and the second is 'odd' if the result is 1, otherwise 'even'.
    """
    remainder = math.fmod(n, 2)  # Mathematically fmod handles negative numbers correctly in Python (returns -1 for odd negatives), but we convert to canonical representation.
    
    # Ensure positive remainder behavior consistent with common "odd/even" checks
    if remainder < 0:
        remainder += 2
        
    parity_str = 'even' if int(remainder) == 0 else 'odd'
    return int(remainder), parity_str

if __name__ == '__main__':
    # Hard-coded sample values; no user input required.
    test_values = [3, -4, 17]

    for val in test_values:
        remainder, description = get_remainder_and_parity(val)
        print(f"Number: {val}, Remainder mod 2: {remainder}, Parity: {description}")