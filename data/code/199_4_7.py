def count_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def sort_names_by_vowel_count(names):
    return sorted(names, key=count_vowels, reverse=True)

if __name__ == '__main__':
    sample_names = ["Adam", "Brian", "Cindy", "Derek"]
    sorted_names = sort_names_by_vowel_count(sample_names)
    print(sorted_names)