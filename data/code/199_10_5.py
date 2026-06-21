names = ["Alice", "Bob", "Charlie", "David", "Eve"]

long_names = [name for name in names if len(name) > 5]

if __name__ == '__main__':
    print(long_names)