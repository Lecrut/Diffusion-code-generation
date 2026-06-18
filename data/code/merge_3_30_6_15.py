def swap_adjacent(s: str) -> str:
    """Swap adjacent characters in a string."""
    chars = list(s)
    result_chars = []
    i = 0
    while i < len(chars):
        if i + 1 < len(chars):
            # Swap current and next character, then advance by 2
            result_chars.append(chars[i])
            result_chars.append(chars[i+1])
            i += 2
        else:
            # Handle last odd element without a pair to swap with (or just append if logic differs)
            # Assuming strict pairwise swap only works for even length or ignores the last one.
            # To strictly "swap adjacent", we take pairs [i, i+1]. If len is odd, the last char remains.
            result_chars.append(chars[i])
        return "".join(result_chars)

def main():
    sample = "abcdef"

if __name__ == '__main__':
    pass
