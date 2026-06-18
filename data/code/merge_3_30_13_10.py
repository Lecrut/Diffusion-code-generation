def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    return "".join([s[i:i+2][::-1] if i % 2 == 0 else s[i-1:i+1][::-1] for i in range(0, len(s), 2)])

# Correct and optimal approach using slicing directly on the original string logic:
def swap_adjacent_chars_v2(s: str) -> str:
    """Swaps all adjacent characters (e.g., 'ab' becomes 'ba', 'cd' remains as is if odd length)."""
    result = []
    for i in range(0, len(s), 2):
        # Take two characters at a time and reverse them
        chunk = s[i:i+2]
        result.append(chunk[::-1])
    return "".join(result)

# Even simpler version using list comprehension directly on the string logic:
def swap_adjacent_chars_final(s: str) -> str:
    """Swaps all adjacent characters in a given string."""
    chars = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            chars.append(f"{s[i+1]}{s[i]}")

if __name__ == '__main__':
    pass
