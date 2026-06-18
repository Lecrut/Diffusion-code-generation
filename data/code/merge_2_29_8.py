def student_generator(names):
    for name in names:
        yield name
if __name__ == '__main__':
    students = ["Alice", "Bob", "Charlie", "David"]
    gen = student_generator(students)
    while True:
        try:
            print(next(gen))
        except StopIteration:
            break