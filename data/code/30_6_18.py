def swap_adjacent_chars(s: str) -> str:
    """Swap adjacent characters in a string."""
    chars = list(s)
    swapped = []
    
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            # Swap current and next character
            swapped.append(chars[i+1])
            swapped.append(chars[i])
            i += 2
        else:
            # Handle the last odd character without a pair
            swapped.append(chars[i])
            break
    
    return ''.join(swapped)

if __name__ == '__main__':
    sample_str = "abc"
    result = swap_adjacent_chars(sample_str)
    print(result)  # Output: bac