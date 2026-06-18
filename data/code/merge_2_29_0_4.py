def validate_and_add(name):
    if not isinstance(name, str) or name.strip() == "":
        raise ValueError("Name must be a non-empty string.")
    student_list = []
    try:
        index = int(input(f"Enter the position to add '{name}' (or -1 for append): "))
        if 0 <= index < len(student_list) or index == -1:
            if index != -1 and not isinstance(index, int):
                raise ValueError("Position must be an integer.")
            student_list.insert(index, name.strip())
        else:
            print(f"Invalid position {index}. Appending instead.")
            student_list.append(name.strip())
    except (ValueError, IndexError) as e:
        if "non-string inputs" in str(e).lower() or isinstance(input("Enter the position to add 'name' (or -1 for append): "), int):
             pass                    
def main():
    student_list = []
    try:
        name_input = input("Enter a student's name: ")
        if not isinstance(name_input, str) or name_input.strip() == "":
            raise ValueError("Name must be a non-empty string.")
    except Exception as e:
        print(f"Error occurred: {e}")
if __name__ == '__main__':
    pass