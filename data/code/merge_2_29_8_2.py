def student_generator(names):
    for name in names:
        yield name
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "David", "Eve"]
    gen_obj = student_generator(students)
    for name in gen_obj:
        print(name)