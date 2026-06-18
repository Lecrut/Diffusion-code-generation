def is_larger(a: float | int, b: float | int) -> bool:
    """
    Returns True if `a` is strictly larger than `b`, otherwise False.

    Parameters:
        a (float or int): The first number to compare.
        b (float or int): The second number to compare.

    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    sample_a = 10
    sample_b = 5

    result = is_larger(sample_a, sample_b)
    print(f"Is {sample_a} larger than {sample_b}?")
    if result:
        print("True")
    else:
        print("False")