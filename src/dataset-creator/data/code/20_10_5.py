def read_student_names(filename):
    student_names = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                student_names.append(line.strip())
        return student_names
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
if __name__ == '__main__':
    file_name = 'students.txt'
    try:
        with open(file_name, 'r') as file:
            names = [line.strip() for line in file]
            print(names)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")