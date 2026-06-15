def read_student_names(filename):
    student_names = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                student_names.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        return None
    return student_names
if __name__ == '__main__':
    file_name = 'students.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("Alice\n")
            f.write("Bob\n")
            f.write("Charlie\n")
            f.write("  Diana  \n")
    except IOError as e:
        print(f"Error writing sample file: {e}")
    names = read_student_names(file_name)
    if names is not None:
        print("Student Names:")
        for name in names:
            print(name)