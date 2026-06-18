from typing import List
def sort_by_length(names: List[str]) -> List[str]:
    return sorted(names, key=len)
def sort_alphabetically(names: List[str]) -> List[str]:
    return sorted(names, key=str.lower)
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    print("Sorted by length:", sort_by_length(sample_names))
    print("Sorted alphabetically:", sort_alphabetically(sample_names))