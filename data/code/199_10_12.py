names = ["Alice", "Bob", "Charlie", "alice", "Bob"]

if __name__ == '__main__':
    filtered_names = [name for name in names if len(name) > 5]
    print(filtered_names)