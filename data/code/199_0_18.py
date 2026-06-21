def validate_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All elements in the list must be strings")

def process_names(names):
    validate_names(names)
    return sorted(set(name.upper() for name in names), reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))