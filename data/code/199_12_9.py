names = ["Alice", "bob", "Charlie", "dave"]

def sort_names(names):
    return sorted(names, key=lambda name: name.lower())

if __name__ == '__main__':
    sorted_names = sort_names(names)
    print(sorted_names)