def are_chars_distinct(text: str) -> bool:
    OCCURRENCE_TRACKER = dict()
    SEEN_MARKER = 1
    for char in text:
        if char in OCCURRENCE_TRACKER:
            OCCURRENCE_TRACKER[char] += 1
        else:
            OCCURRENCE_TRACKER[char] = SEEN_MARKER
    return all(val == SEEN_MARKER for val in OCCURRENCE_TRACKER.values())

if __name__ == '__main__':
    sample_1 = "python"
    sample_2 = "banana"
    print(are_chars_distinct(sample_1))
    print(are_chars_distinct(sample_2))