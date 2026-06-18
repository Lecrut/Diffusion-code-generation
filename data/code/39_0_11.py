import re

def extract_all_substrings(text: str, desired_patterns: list) -> list:
    """
    Extracts all occurrences of patterns from a string in order.

    This function attempts to match each pattern individually against the text 
    and collects every occurrence found, preserving their relative order based 
    on the start index in the original text. Patterns are treated as simple substrings; 
    if exact matching is desired with potential regex-like behavior (e.g., special characters),
    this implementation supports basic patterns directly or can be adapted for regex by replacing '^' and '$'.

    Args:
        text (str): The source string to search within.
        desired_patterns (list[str]): A list of strings representing the substrings 
                                     to find in the text. Each substring is searched independently,
                                     but results are merged into a single ordered sequence based on position.

    Returns:
        list[dict]: A list of dictionaries where each dictionary contains 'pattern' and 'indices'.
                   Example: [{'pattern': 'abc', 'indices': [(12,), (45,)]}] for "text abc more abc" given patterns=['abc']".

def extract_all_substrings(text: str, desired_patterns: list[str]) -> list[dict]:
    """

if __name__ == '__main__':
    pass
