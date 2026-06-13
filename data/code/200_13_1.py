def filter_names(names):
    return [name for name in names if name.startswith('A')]
if __name__ == '__main__':
    user_names = ["Alice", "Bob", "Andrew", "Charlie", "Adam", "Anna"]
    a_names = filter_names(user_names)
    print(a_names)