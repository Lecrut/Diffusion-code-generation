def count_vowels(string_list):
    """
    Accepts a list of strings and returns a dictionary where:
        - Keys are the input strings.
        - Values are the counts of vowels in each string (case-insensitive).
    
    Vowels considered: 'a', 'e', 'i', 'o', 'u'.
    """
    vowels = set('aeiouAEIOU')
    result_dict = {}

    for item in string_list:
        count = sum(1 for char in item if char in vowels)
        result_dict[item] = count
    
    return result_dict

if __name__ == '__main__':
    sample_data = ["Hello", "World", "Python", "AEIOU", "aeiou"]
    
    output = count_vowels(sample_data)

    print("Input:", sample_data)
    print("Output dictionary:")
    for k, v in output.items():
        print(f"'{k}': {v}")