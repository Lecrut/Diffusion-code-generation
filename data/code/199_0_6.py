def convert_to_uppercase(names):
    return [name.upper() for name in names]

def remove_duplicates(names):
    return list(set(names))

def sort_in_descending_order(names):
    return sorted(names, reverse=True)

def process_names(names):
    upper_names = convert_to_uppercase(names)
    unique_names = remove_duplicates(upper_names)
    sorted_names = sort_in_descending_order(unique_names)
    return sorted_names

if __name__ == '__main__':
    sample_names = ['Eve', 'adam', 'Charlie', 'eve', 'Adam']
    processed_names = process_names(sample_names)
    print(processed_names)