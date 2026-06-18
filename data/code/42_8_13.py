"""
Script demonstrating string construction using list comprehension and str.join().
This script avoids building intermediate concatenated strings in a loop (inefficient) 
by generating parts first, then joining them once with an optimized method.
"""

def build_sentence():
    """
    Constructs a final sentence from individual word parts stored in lists.
    
    Optimization Strategy:
    Instead of repeatedly concatenating substrings using the + operator inside a loop,
    which creates new string objects on every iteration (O(n^2) complexity), we use 
    list comprehension to create a unified list of words and then call str.join().
    The join() method iterates over the input only once, making it O(n).
    
    Args: None
    
    Returns: A single concatenated string.
    """
    # List 1 contains nouns or subjects (hardcoded sample data)
    subject_parts = ["The", "quick"]
    
    # Using list comprehension to append adjectives from another source list 
    # to the first list dynamically, creating a new unified list of parts.
    adjective_source_list = ["brown"]
    full_subjects = [part for part in subject_parts if part != ""] + \
                    [adj for adj in adjective_source_list if adj not in ("", "")]
    
    # List 2 contains verbs or actions (hardcoded sample data)
    verb_part = ["jumps"]
    
    # Using list comprehension to add the verb and object parts.
    full_verb_objects = ([part for part in verb_part] + 
                         [obj for obj in ("over", "the") if obj not in ("", "")])
        
    final_words_list = []
    
    # Appending the complete subject phrase into our main list of words to join later.
    # We assume 'full_subjects' acts as a segment and append it element-wise 
    # or treat it directly depending on structure; here we flatten logic for clarity:
    full_text_parts = [part for part in (" ".join(full_subjects) + " ").split() if part] \
                        + ([p for p in (full_verb_objects[0]) if p != ""], 
                           *(" ".join(full_verb_objects)).split()[1:]) 
    
    # Correction to ensure we simply join the final list cleanly:
    raw_parts = ("The", "quick") + tuple(["brown"]) + \
                ["jumps"] + ("over", "the") if True else []

    return "".join(raw_parts).strip()

if __name__ == '__main__':
    # Hard-coded sample values ensuring the script runs without user input or external dependencies.
    
    result_string = build_sentence()
    
    print("Optimized String Construction Result:")
    print(result_string)