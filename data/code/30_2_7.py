def swap_adjacent_pairs(s: str) -> str:
    """Swap all adjacent character pairs in the string."""
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            # Swap current and next pair characters
            result.append(s[i+1])
            result.append(s[i])
            i += 2
        else:
            # Odd length string, append the last character as is
            result.append(s[i])
            break
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "ab",
        "xyz",
        "123456",
        "",
        "abcde"
    ]
    
    for s in sample_strings:
        modified_s = swap_adjacent_pairs(s)
        print(modified_s)