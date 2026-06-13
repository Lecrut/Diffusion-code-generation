def filter_names(names):
    return [name for name in names if name.startswith('A')]
if __name__ == '__main__':
    user_names = ["Alice", "Bob", "Anna", "Charlie", "Adam", "David"]
    result = filter_names(user_names)
    print(result)