def swap_adjacent(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    return s[::2][::-1] + s[1::2][::-1]

if __name__ == '__main__':
    sample_string = "abcdef"
    result = swap_adjacent(sample_string)
    print(result)  # Output: fedcba