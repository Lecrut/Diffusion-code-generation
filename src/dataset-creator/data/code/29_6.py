from typing import List
def sort_by_length(names: List[str]) -> List[str]:
    return sorted(names, key=len)
def sort_alphabetically(names: List[str]) -> List[str]:
    return sorted(names, key=str.lower)
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "David"]
    print("Original:", students)
    print("Sorted by length:", sort_by_length(students))
    print("Sorted alphabetically:", sort_alphabetically(students))