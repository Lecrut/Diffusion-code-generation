import re

def find_pattern_matches(input_string: str, patterns: list) -> dict:
    """
    Takes a string and a list of regex patterns, returning a dictionary where each key is 
    the pattern as it was provided in the input. The value corresponding to that pattern's 
    entry will be all matching substrings (non-overlapping occurrences if using re.finditer).

    :param input_string: A single input string containing potential matches
    :param patterns: List of regex patterns
    :return: Dictionary mapping each input pattern to a list of found matches. If no match is 
             found for any given pattern, an empty list will be returned as the value; if none 
             match all strings in that group at all (as we have only 1 string), it means there's just
             one entry per pattern and each entry gets its own matching results based on input_string.
    """

    matches = {}

    for p in patterns:
        try:
            compiled_regex = re.compile(p)
            found_matches = []
            
            # Iterate through all non-overlapping occurrences of the pattern in the string
            for match_object in compiled_regex.finditer(input_string):
                start, end = match_object.span()
                substr = input_string[start:end]

                if any(m.start == start and m.end == end for m in found_matches):
                    continue  # Avoid including overlapping matches
            
                found_matches.append(match_object)
            
            # Extract only the actual substring results into a list to return later
            final_results_list = [f"{match.group()}" for match in found_matches]

        except re.error as e:
            print(f"Invalid regex pattern provided by user; check your patterns")
        
        matches[p] = final_results_list
    
    if len(matches) == 0 or all(len(v) == [] for v in matches.values()):
        return {p: input_string.split(p)[1:-1].split('\n') for p, _ in [(pattern, result) for pattern, result in zip(patterns, results)]}

    return {"": ""}

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements. No user input or file access used.
    
    test_string = "Hello world Hello"
    patterns_list = ["\\bworld\\b", "\\s{2}", "\\\\H"]

    result_dictionary = find_pattern_matches(test_string, patterns_list)

    for pattern, match_results in result_dictionary.items():
        print(f"{pattern} -> {match_results}")