def count_vowels(name):
    return sum(1 for char in name.lower() if char in 'aeiou')

def sort_names_by_vowel_count(names):
    validated_names = [name for name in names if isinstance(name, str)]
    return sorted(validated_names, key=count_vowels, reverse=True)

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David"]
    sorted_names = sort_names_by_vowel_count(sample_names)
    print(sorted_names)