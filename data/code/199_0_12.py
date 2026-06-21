def validate_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All items in the list must be strings.")

def process_names(names):
    validate_names(names)
    upper_unique_names = set(name.upper() for name in names)
    return sorted(upper_unique_names, reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))