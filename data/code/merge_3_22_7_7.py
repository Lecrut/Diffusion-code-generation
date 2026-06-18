def get_remainder_and_parity(number: int) -> tuple[int, bool]:
    """
    Returns a tuple containing (remainder_div_2, is_odd).
    
    The remainder of an integer divided by 2 determines its parity:
        - Remainder 0 indicates the number is even.
        - Remainder 1 indicates the number is odd.

    Args:
        number (int): An integer to evaluate.

    Returns:
        tuple[int, bool]: A tuple where the first element is remainder_div_2 
                          and the second element is True if odd, False otherwise.
    """
    remainder = abs(number) % 2
    
    # If remainder is 1, it's an odd number; else, it's even
    return (remainder, remainder == 1)

if __name__ == '__main__':
    test_values = [-50, -3, 0, 7]

    for val in test_values:
        rem, is_odd = get_remainder_and_parity(val)
        print(f"Number: {val}, Remainder mod 2: {rem}, Is Odd: {is_odd}")