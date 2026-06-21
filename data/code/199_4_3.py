vowel_counts = {
    'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1,
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1
}

def count_vowels(name):
    return sum(vowel_counts.get(char, 0) for char in name)

def sort_names_by_vowels(names):
    return sorted(names, key=count_vowels, reverse=True)

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = sort_names_by_vowels(sample_names)
    print(sorted_names)