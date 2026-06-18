"""
Module to find all nested substrings within a phrase, handling overlapping cases correctly.
Returns results in a structured list of tuples: (start_index, end_index, substring).
Indices are 0-based and inclusive on both ends.
The algorithm uses an optimized approach that avoids redundant slicing by tracking 
already found occurrences and extending from them where possible to handle overlaps efficiently.

Time Complexity: O(n^2) in the worst case for strings with many overlapping patterns,
but significantly faster than naive repeated scanning due to incremental extension logic.
Space Complexity: O(k), where k is the number of unique substrings identified during processing.
"""

if __name__ == '__main__':
    pass
