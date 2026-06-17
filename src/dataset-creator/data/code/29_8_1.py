def student_generator(names):
    for name in names:
        yield name
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "David"]
    gen_obj = student_generator(students)
    for i, name in enumerate(gen_obj):
        print(f"{i}: {name}")