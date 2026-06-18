def swap_adjacent_chars(s: str) -> str:
    """Swaps adjacent characters in a string using list manipulation."""
    chars = list(s)
    n = len(chars)
    if n % 2 == 1:
        # Last character remains unchanged for odd-length strings
        return "".join([chars[i] for i, _ in enumerate(range(0, n - 1), 2)] + [chars[n-1]])

    for i in range(n // 2):
        chars[2 * i], chars[2 * i + 1] = chars[2 * i + 1], chars[2 * i]
    
    return "".join(chars)

if __name__ == '__main__':
    sample_input = "python"
    result = swap_adjacent_chars(sample_input)
    print(result)  # Output: phtoyn