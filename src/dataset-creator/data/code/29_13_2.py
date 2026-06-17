import sys
def add_student(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if len(name.strip()) == 0:
        return
    students.append(name.strip())
def get_students() -> list[str]:
    return [s for s in students]
def validate_name(name: str) -> bool:
    try:
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        clean = name.strip()
        return all(c.isalnum() or c.isspace() for c in clean)
    except Exception:
        return False
if __name__ == '__main__':
    students: list[str] = []
    add_student("Alice")
    add_student("Bob Smith")
    print(validate_name("Charlie"))        
    print(validate_name("David-123"))                
    retrieved = get_students()
    print(retrieved)