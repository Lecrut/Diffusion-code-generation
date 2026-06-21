def count_vowels(name):
    return sum(1 for char in name.lower() if char in 'aeiou')

def sort_names_by_vowels(names):
    return sorted(names, key=count_vowels, reverse=True)

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    sorted_names = sort_names_by_vowels(sample_names)
    print(sorted_names)