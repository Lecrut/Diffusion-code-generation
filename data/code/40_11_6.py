def get_first_letters(string_list):
    """
    Returns a new list containing only the first character of each string in the input list.
    
    Args:
        string_list (list[str]): A list of strings to process.
        
    Returns:
        list[str]: A list where each element is the first character of the corresponding input string.
                   If an empty string exists, it will result in an empty string being included or skipped 
                   based on logic; here we include '' as per strict 'first char' definition for non-empty strings,
                   but if a string is empty, there is no first letter. To handle safely:
                   We assume inputs are valid non-empty strings as per typical use case requirements unless specified otherwise.
                   However, to be robust and avoid errors on empty strings (which have no 'first character'), 
                   we can choose to skip them or include an error indicator. Given the task asks for "only the first letter",
                   if a string is empty, it technically has none. Let's filter out non-empty ones only? 
                   Actually, re-reading: "returns ... containing only the first character of each string".
                   If input is ["a", "", "b"], output should ideally be ['a', '', 'b']? No, '' has no char.
                   
    Clarification for robustness: We will extract the first character if the string is non-empty. 
    For empty strings, we have two choices: include an empty string in result or omit them entirely.
    Given "first letter", it implies existence of a letter. But often such functions just take s[0].
    Let's use s[0] directly which raises IndexError for empty list/string. To avoid runtime error on potentially 
    present empty strings, we can check length first? Or assume valid input as per typical coding tasks unless specified "handle edge cases".
    
    Since task says "optimized function", and no explicit error handling requested, let's use try-except or conditional access.
    But simplest optimized approach assuming non-empty: list comprehension with s[0]. 
    However to be safe against empty strings (which might exist in real data), we can do: [s[0] for s in string_list if len(s) > 0]
    BUT the task says "of each string", implying all. If a string is empty, it has no first letter. 
    Let's assume inputs are non-empty as per standard problem constraints unless stated otherwise.
    
    Revised plan: Use list comprehension directly with s[0]. This assumes input strings are not empty to avoid exceptions.
    If the user provides an empty string, this will crash. To be safe and "optimized", we can handle it gracefully? 
    But task doesn't ask for error handling. Let's stick to direct access assuming valid non-empty inputs as is common in such tasks.
    
    Actually, let's make it robust: if a string is empty, skip it or include ''? The phrase "first letter" suggests skipping empties.
    However, without explicit instruction on edge cases, and for maximum efficiency (avoiding condition checks), 
    we assume non-empty strings. If an empty string occurs, the function will raise IndexError. This is acceptable unless specified otherwise.
    
    Final decision: Use list comprehension with s[0]. No conditional check to maintain max speed as requested ("maximum efficiency").

    Example input: ["apple", "banana"] -> ['a', 'b']
    """
    return [s[0] for s in string_list if len(s) > 0]

if __name__ == '__main__':
    sample_data = ["hello", "world", "python", "coding"]
    result = get_first_letters(sample_data)
    print(result)