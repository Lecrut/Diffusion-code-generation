def run_length_encode_alphanumeric(s):
    alnum_seq = [c for c in s if c.isalnum()]
    if not alnum_seq:
        return {}
    sequence_counts = []
    current = alnum_seq[0]
    run = 1
    for char in alnum_seq[1:]:
        if char == current:
            run += 1
        else:
            sequence_counts.append((current, run))
            current = char
            run = 1
    sequence_counts.append((current, run))
    final_map = {}
    for ch, cnt in sequence_counts:
        if ch in final_map:
            final_map[ch] += cnt
        else:
            final_map[ch] = cnt
    return final_map

if __name__ == '__main__':
    sample_input = "aaabbbccc111!@#aabb"
    print(run_length_encode_alphanumeric(sample_input))