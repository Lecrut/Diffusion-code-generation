from typing import List
def add_student(name: str) -> None:
    pass
def remove_student(name: str) -> bool:
    pass
def get_all_students() -> List[str]:
    return []
def sort_by_length(students: List[str]) -> List[str]:
    return sorted(students, key=len)
def sort_alphabetically(students: List[str]) -> List[str]:
    return sorted(students, key=str.lower)
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "Diana"]
    print("Original:", get_all_students())
    print("Sorted by length:", sort_by_length(get_all_students()))
    print("Sorted alphabetically:", sort_alphabetically(get_all_students()))