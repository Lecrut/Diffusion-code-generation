def filter_names_by_initial(names, initial):
    return (name for name in names if name.startswith(initial))

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    initial_letter = 'A'
    filtered_names = filter_names_by_initial(sample_names, initial_letter)
    print(list(filtered_names))