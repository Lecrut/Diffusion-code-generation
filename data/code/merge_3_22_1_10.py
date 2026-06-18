def is_odd(n: int) -> bool:
    """Return True if n is odd, False otherwise."""
    return n % 2 != 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [1, -3, 0, 4, 7, -8]
    
    print("Testing 'is_odd' function:\n")
    for num in samples:
        result = is_odd(num)
        status = "ODD" if result else "EVEN"
        print(f"{num}: {status}")