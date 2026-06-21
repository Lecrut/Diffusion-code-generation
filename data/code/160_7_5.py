def filter_duplicates(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    return unique_names

if __name__ == '__main__':
    item_names = ["Apple", "Banana", "Cherry", "Apple", "Fig", "Grape"]
    filtered_names = filter_duplicates(item_names)
    print(filtered_names)