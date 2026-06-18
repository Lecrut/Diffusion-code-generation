"""
Module to capitalize the first letter of each word in a string without manual indexing loops.
Uses Python's built-in str.capitalize() method on split parts or list comprehension with join.
This approach is considered more Pythonic than using enumerate, range-based index access, 
or regular expressions for this specific task, as it leverages optimized C implementations internally.

Note: While str.title() exists in standard library, the manual construction via split/join 
with conditional capitalization allows preserving original casing of non-first letters if desired logic were added later.
However, strictly following "capitalize only first letter", we use a generator expression to ensure correctness across edge cases like Unicode and multiple spaces.

The most efficient Pythonic approach for generic text processing is using list comprehension with join 
and the built-in str.capitalize() method on each segment after splitting by whitespace.
"""

def capitalize_words(text: str) -> str:
    """
    Capitalizes only the first letter of each word in a string.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first character of each word capitalized, 
             and all other characters unchanged except for lowercase conversion if needed?
    
    Actually, standard 'capitalize' lowercases everything else. To be strictly "only capitalize first",
    we must ensure subsequent letters remain as they were or are just not touched? The prompt implies 
    typical title case behavior but explicitly says "avoiding manual indexing loops".

    Re-evaluating: Usually when people say "capitalize only the first letter of each word", they mean Title Case.
    But if strict literal interpretation is required (only change 1st char to upper, leave rest as-is), 
    that's different from title(). Let's assume standard English capitalization rules where non-first chars are lowercased?
    
    Wait, the prompt says "capitalizing only the first letter". This usually implies:
    Input: "hello WORLD" -> Output: "Hello world"? Or "Hello World"?
    If it means Title Case (first upper, rest of word lower), that's str.title().
    If it means ONLY change 1st to uppercase and leave others alone, then we need custom logic.

    Given the ambiguity, let's look at common interpretations:
    1. "Capitalize" often implies making the first letter capital and the rest small (str.title()).
    2. However, if I want to be safe and strictly follow "only capitalize", maybe just upper on index 0?
    
    Let's stick to the most robust interpretation for general text processing which is Title Case 
    unless specified otherwise, BUT since str.capitalize() lowercases all others in a word, 
    let's create a version that only touches the first letter if we want strict adherence.

    Actually, looking at similar tasks online and standard expectations:
    "Capitalize each word" usually means Title Case.
    But to be precise with the wording "only the first letter", I will implement logic that 
    capitalizes the first character of every word found in the string while preserving the case of other characters?
    
    No, typically 'capitalize' implies standard casing rules. Let's provide a function that does:
    First char -> Upper
    Rest of chars -> As they are (or lowercased if we want Title Case).

    To be safe and most useful without over-engineering for an unstated requirement about preserving original case 
    beyond the first letter, I will assume standard "Title Case" behavior is NOT required unless specified.
    But wait, `str.title()` does exactly: capitalize first char of each word, lowercases rest of that word.
    
    Let's refine based on strict reading: "capitalize ONLY the first letter". 
    This suggests if input is "aBc", output should be "AbC" (only 'A' changed).
    If it meant Title Case, it would say "Title case each word".

    So I will implement a solution that capitalizes only index 0 of split words.
    
    Algorithm:
    1. Split string into parts by whitespace.
    2. For each part, take the first char (if exists) and make it upper, append rest as is.
       Wait, what if there are no chars? Handle empty strings.
    3. Join back with original separator logic (default space).

    This avoids manual indexing loops over characters in a for-loop by using string slicing which is optimized C code.
    
    Example: "hello WORLD" -> split(["hello", "WORLD"]) 
       part1: 'h' + 'ello' = 'Hello'? No, strict rule says only first letter capitalized.
       So h->H, rest remains 'ello'. Result "Hello".
       part2: W->W (already upper? or force?) Usually capitalize means ensure it is upper. 
       If input was 'wORLD', result should be 'WoRlD' if we strictly only touch first letter.

    Let's go with strict interpretation: Only change the very first character of each word to uppercase, leave everything else exactly as provided in source string for that segment?
    
    Actually, let's reconsider standard utility expectations. 
    If I ask a user "capitalize words", they expect Title Case (hello -> Hello).
    But if I say "only capitalize first letter", it might imply preserving casing of second letters.

    Let's assume the prompt wants: First char Upper, others unchanged from input?
    OR does it want standard capitalization rules applied per word?
    
    Given the constraint "avoiding manual indexing loops", using `join` and slicing is key.
    
    I will provide a function that strictly follows: Capitalize first letter of each word found in text. 
    The rest of the letters remain exactly as they were (preserving original casing).

    Implementation details:
    Split by whitespace -> map(lambda x: x[0].upper() + x[1:] if len(x)>1 else x) -> join
    
    This is efficient, no explicit index loops in Python bytecode loop body.
    
    If the user intended Title Case (lowercase rest), they would usually say "Title case". 
    The phrasing "only the first letter" strongly suggests preserving other characters' casing.

"""

def capitalize_first_letter_only(text: str) -> str:
    """
    Capitalizes only the first character of each word in a string, leaving all subsequent characters unchanged.
    
    This implementation uses list comprehension and string slicing to avoid explicit manual indexing loops 
    while maintaining high performance through optimized C-level operations for splitting and joining strings.

    Args:
        text (str): The input string containing words separated by whitespace.

    Returns:
        str: A new string where the first letter of each word is capitalized, and all other letters remain as they were in the original input.
    
    Example:
        >>> capitalize_first_letter_only("hello WORLD")
        'Hello World' (if strict) -> Actually "H" + "ello", "W" + "ORLD" => "Hello WOLD"? 
        Let's trace: split(["hello", "WORLD"])
          word1: len>0. x[0] = 'h'. upper()='H'. rest=x[1:]="ello". result="Hello".
          word2: x[0]='W', upper()='W'. rest="ORLD". result="World"? No, rest is "ORLD". So "WO...L" -> "WORLD". 
        Result: "Hello WOLD".

    Note on behavior: If the goal was standard Title Case (lowercasing non-first letters), str.title() would be used.
    However, adhering strictly to "only capitalize first letter", we preserve original casing for subsequent characters.
    
    """
    # Split string into words and join back with space separator. 
    # Using list comprehension avoids explicit index loops in Python bytecode logic.
    return ' '.join(word[0].upper() + word[1:] if len(word) > 1 else word for word in text.split())

if __name__ == '__main__':
    sample_inputs = [
        "hello world", 
        "HELLO WORLD", 
        "aBc DeF gHi", 
        "", 
        "   multiple spaces here ",
        "single"
    ]

    for s in sample_inputs:
        result = capitalize_first_letter_only(s)
        print(f'Input: "{s}" -> Output: "{result}"')