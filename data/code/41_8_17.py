def format_string(s):
    """
    Takes a string and returns a formatted string containing:
    1. The original input
    2. All-caps version of the input (using str.upper())
    3. Sentence-case version using logic similar to title case but preserving 
       internal casing for acronyms or specific rules if needed, though strictly
       sentence-case usually implies capitalizing only words that would start sentences.
       For this task, we will interpret 'sentence-case' as Title Case (each word capitalized)
       since standard library doesn't have a dedicated reverse-sentence-transformer that 
       guarantees exact original casing logic for mid-word changes without complex parsing.
       However, to strictly follow "built-in methods", str.title() is the closest fit 
       representing sentence case conventions where every major character after spaces is uppercased.

    Args:
        s (str): The input string.

    Returns:
        str: A formatted string with original, all-caps, and sentence-case versions separated by commas.
    """
    uppercase_version = s.upper()
    
    # Using built-in title method to simulate sentence case where each word starts with a capital letter
    lowercase_original = s.lower()
    # Reconstruct simple sentence-like casing: Capitalize the first character of each word found via split/join or simply using title().
    # Since str.title() handles non-ascii and multiple spaces reasonably well for this context, we use it.
    sentence_version = s.title()

    return f"{s}, {uppercase_version}, {sentence_version}"

if __name__ == '__main__':
    sample_input = "hello world"
    result = format_string(sample_input)
    print(result)