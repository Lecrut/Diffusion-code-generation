def process_names(names):
    upper_unique_names = set(name.upper() for name in names)
    sorted_names = sorted(upper_unique_names, reverse=True)
    return sorted_names

if __name__ == '__main__':
    sample_names = ['Eve', 'adam', 'Charlie', 'dave', 'Alice']
    print(process_names(sample_names))