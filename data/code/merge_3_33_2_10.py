import sys

def remove_all_spaces(text: str) -> str:
    """Remove all internal and external spaces from a string."""
    return ''.join(filter(str.strip, text.replace(' ', '')))  # Replace spaces first to catch multi-line gaps if any exist between chars, but the main goal is stripping. Actually, re-reading "internal" usually means characters inside words? No, standard interpretation in this context (often from coding challenges) for "eliminate all internal and external spaces" on a string usually implies:
    # 1. Remove leading/trailing whitespace entirely.
    # 2. Remove any sequence of multiple whitespace characters between text segments as if it were one space? OR remove ALL spaces completely to get just letters/numbers/symbols concatenated?
    
    # The prompt says "completely eliminated". This strongly suggests the output should have ZERO spaces left, not reduced to single ones.
    return ''.join(text.split())  # split() with no args splits by any whitespace (newlines included) and strips empty strings

# Note: 'text.strip()' handles external. '.split()' handles internal sequences of newlines/spaces. 
# Then joining them eliminates the separators entirely if we want "completely eliminated".
# Let's verify interpretation: "internal ... spaces completely eliminated" vs "reduced to single space".
# If I have "a b", split() -> ['a', 'b'], join -> 'ab'. Spaces removed. Correct.
# If I have "\n\n a \nb ", strip+split -> [], join -> empty? No, "  ".strip().split() is []. 
# But for multi-line: "line1\n line2". split(' ') might keep the newline char if not handled by regex logic of split with whitespace.
# Python's str.split() without arguments treats any string of whitespace (including \n) as a delimiter.
# So "a\nc" -> ['a', 'c'] -> join -> 'ac'. This eliminates internal newlines/spaces too.

    # Re-implementation for explicit clarity matching the request exactly:
def remove_all_spaces_v2(text):
    """Remove all whitespace characters (spaces, tabs, newlines) from string."""
    return ''.join(char if char not in ' \t\n\r' else '' for char in text)

if __name__ == '__main__':
    # Hard-coded sample values as per instructions to avoid input() or sys.stdin read calls.
    # Simulates reading a multi-line string from standard input but hard-codes it directly.
    sample_input = "Hello World\n  This is   a test \n String."

    result_str = remove_all_spaces_v2(sample_input)

    print(result_str)