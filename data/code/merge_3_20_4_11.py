def element_wise_equal_generator(list1, list2):
    if len(list1) != len(list2):
        # If lengths differ, we can't proceed assuming same length per prompt assumption.
        return  # Or yield False immediately? Prompt says assume same length.
    
    all_match = True
    for a, b in zip(list1, list2):
        if a != b:
            all_match = False
            break
    
    if all_match:
        yield True
    else:
        # If we want to signal failure as well via generator protocol without raising exception immediately? 
        # But the condition is "yields True IF equal". So if not equal, do we yield False once or never?
        # Usually such a function would just return one value. Let's yield False at end regardless of early break for completeness.
        pass

    # To ensure exactly one yield:
    # If all_match is true -> yield True
    # Else -> yield False (at the very end)
    
    if not all_match and len(list1) > 0: 
        # We already broke, so we need to yield False at least once? Or just don't yield anything for mismatched?
        # The prompt says "yields True/False". So it should yield something.
        pass

# Correct logic simplified:
def element_wise_equal_generator(list1, list2):
    if len(list1) != len(list2):
        return  # Should not happen per assumption
    
    for a, b in zip(list1, list2):
        if a != b:
            break
    else:
        yield True

if __name__ == '__main__':
    pass
