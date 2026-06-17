def sort_students(*names):
    return tuple(sorted(names))
if __name__ == '__main__':
    students = ("Alice", "Bob", "Charlie")
    print(sort_students(*students))