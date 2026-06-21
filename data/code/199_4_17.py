def sort_names_by_vowels(names):
    return sorted(names, key=lambda name: sum(1 for char in name.lower() if char in 'aeiou'), reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'David']
    print(sort_names_by_vowels(sample_names))