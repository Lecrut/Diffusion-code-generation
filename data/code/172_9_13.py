lookup_words = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five"
}

def initialize_dictionary(start, end):
    dictionary = {}
    for i in range(start, end + 1):
        if i in lookup_words:
            dictionary[i] = lookup_words[i]
    return dictionary

if __name__ == '__main__':
    sample_dict = initialize_dictionary(1, 5)
    print(sample_dict)