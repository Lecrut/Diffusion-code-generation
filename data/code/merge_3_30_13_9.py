def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    return ''.join([s[i] + s[i+1] if i % 2 == 0 else '' 
                    for i, ch in enumerate(list(s))])

if __name__ == '__main__':
    sample_input = "abcdef"
    result = swap_adjacent_chars(sample_input)
    print(result)