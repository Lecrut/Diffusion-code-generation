import functools
from collections import Counter
def sort_fruits(fruit_data):
    fruit_types = [f.split()[0] for f in fruit_data]
    counts = {ft: sum(1 for ft_list in fruit_types if ft_list == ft) for ft in set(fruit_types)}
    sorted_fruits = sorted(set(fruit_types), key=lambda x: (x, counts[x]))
def main():
    sample_input = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon"
    ]
    unique_fruits = list(set(sample_input))
    if __name__ == '__main__':
        print(sorted(unique_fruits, key=lambda x: (x, sample_input.count(x) * 0.1)))
if __name__ == "__main__":
    main()