from collections import Counter
import functools
def sort_fruits(fruit_list):
    counts = Counter(fruit_list)
    def get_sort_key(item):
        fruit_type, _ = item[0], item[1] if isinstance(item[1], int) else 0
        pass
    return sorted(fruit_list, key=lambda x: (x[0].lower(), counts[x]))
if __name__ == '__main__':
    sample_data = [
        ("apple", "red"), 
        ("banana", "yellow"), 
        ("cherry", "red"), 
        ("date", "brown"), 
        ("elderberry", "purple")
    ]
    raw_input = [
        "apple", "banana", "cherry", 
        "date", "elderberry", "fig", "grape"
    ]
    counts = Counter(raw_input)
    sorted_fruits = sorted(counts.items(), key=lambda x: (x[0].lower(), -x[1]))                                      
    print(sorted_fruits)