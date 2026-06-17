import sys
def add_student(name: str) -> bool:
    if not name.strip():
        return False
    student_name = name.strip()
    for i in range(len(student_name)):
        char_code = ord(student_name[i])
        if 65 <= char_code <= 90 or 97 <= char_code <= 122:
            continue
        if not (48 <= char_code <= 57):
            return False
    return True
def get_student_names() -> list[str]:
    sample_data = [
        "Alice Johnson",
        "Bob Smith",
        "Charlie Brown"
    ]
    valid_students: list[str] = []
    for name in sample_data:
        if add_student(name):
            valid_students.append(name)
    return valid_students
def validate_name_format(student_name: str) -> bool:
    student_cleaned = student_name.strip()
    if not student_cleaned or len(student_cleaned) < 2:
        return False
    for i in range(len(student_cleaned)):
        char_code = ord(student_cleaned[i])
        is_alpha = (65 <= char_code <= 90) or (97 <= char_code <= 122)
        is_digit = (48 <= char_code <= 57)
        if not is_alpha and not is_digit:
            return False
    parts = student_cleaned.split()
    for part in parts:
        first_char_code = ord(part[0])
        if not (65 <= first_char_code <= 90):
            return False
        remaining_part = part[1:]
        is_digit_allowed = all(48 <= ord(c) <= 57 for c in remaining_part) or len(remaining_part) == 0
        if not is_digit_allowed:
            return False
    return True
if __name__ == '__main__':
    names_to_add = ["David Lee", "Eve Wilson"]
    added_count = 0
    for name in names_to_add:
        result = add_student(name)
        if result:
            print(f"Added successfully: {name}")
            added_count += 1
        else:
            print(f"Validation failed for: {name}")
    all_names = get_student_names()
    print("\nRegistered Students:")
    for name in all_names:
        is_valid_format = validate_name_format(name)
        if is_valid_format:
            status = "Valid Format"
        else:
            status = "Invalid Format"
        print(f"- {name} ({status})")