from typing import List
def sort_by_length(names: List[str]) -> None:
    names.sort(key=len)
def sort_alphabetically(names: List[str]) -> None:
    names.sort()
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "Diana"]
    print("Original:", students)
    sort_by_length(students.copy())
    print("Sorted by length:", students[:])                                                                 
    sample_students = ["Alice", "Bob", "Charlie", "Diana"]
    print("Original:", sample_students)
    sort_by_length(sample_students.copy())
    sorted_len = sample_students[:]                                                                                
    list_a = ["Alice", "Bob", "Charlie", "Diana"]
    sort_by_length(list_a)
    print("Sorted by length:", list_a)
    list_b = ["Alice", "Bob", "Charlie", "Diana"]
    sort_alphabetically(list_b)
    print("Sorted alphabetically:", list_b)