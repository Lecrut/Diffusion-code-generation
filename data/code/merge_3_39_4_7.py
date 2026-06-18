import re

def split_by_delimiters(phrase: str, delimiters: set) -> list[str]:
    """
    Splits a phrase into all contiguous segments separated by any character 
    present in the provided delimiter set.

    Args:
        phrase (str): The input string to be split.
        delimiters (set of str): A set containing single-character strings representing delimiters.

    Returns:
        list[str]: A list of non-empty contiguous segments separated by any character from `delimiters`.
    
    Note: 
    - Empty or whitespace-only segments are excluded unless explicitly requested via custom empty string handling, 
      but based on standard behavior for splitting, consecutive delimiters result in no segment between them.
    """
    if not phrase and not delimiters:
        return []

    # Escape special regex characters to safely use re.split

if __name__ == '__main__':
    pass
