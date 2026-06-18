def sort_students(*names):
    return tuple(sorted(names))
if __name__ == '__main__':
    students = ("Alice", "Bob", "Charlie", "David")
    result = sort_students(*students)
    print(result)