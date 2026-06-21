names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

filtered_names = [name for name in names if len(name) > 5]

if __name__ == '__main__':
    print(filtered_names)