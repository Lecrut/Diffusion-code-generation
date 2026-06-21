def filter_names_by_initial(names, initial):
    return (name for name in names if name.startswith(initial))

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    filtered_names = filter_names_by_initial(sample_names, 'A')
    print("Filtered names:", list(filtered_names))