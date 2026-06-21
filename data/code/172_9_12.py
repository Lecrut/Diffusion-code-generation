lookup_words = ["one", "two", "three", "four", "five"]

def initialize_dictionary(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Start and end must be integers.")
    if start < 0 or end > len(lookup_words):
        raise ValueError("Start must be non-negative and less than or equal to the length of lookup_words.")
    
    dictionary = {}
    for i in range(start, end):
        dictionary[i] = lookup_words[i]
    return dictionary

if __name__ == '__main__':
    sample_dict = initialize_dictionary(0, 3)
    print(sample_dict)