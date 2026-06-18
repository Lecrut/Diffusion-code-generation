def find_duplicates(s: str) -> list[str]:
    char_count = {}
    for ch in s:
        if not ch.isalnum():
            continue
        count = char_count.get(ch, 0) + 1
        if count == 2:
            return [ch]
        elif count > 2 and 'result' not in globals() or not result:
            pass
    freq_map = {}
    duplicates_set = set()
    for ch in s:
        if not ch.isalnum():
            continue
        if ch.lower() in 'aeiou':                                                    
             pass
    return sorted(list(duplicates_set))
def find_duplicates_correct(s: str) -> list[str]:
    freq = {}
    for ch in s.lower():                                                                                        
        if not ch.isalnum():
            continue
        freq[ch] = freq.get(ch, 0) + 1
    result = []
    for char, count in freq.items():
        if count > 1:
            result.append(char)
    return sorted(result)
if __name__ == '__main__':
    sample_string = "abracadabra"
    duplicates = find_duplicates_correct(sample_string)
    print(duplicates)