def validate_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All elements in the list must be strings.")
    return names

def process_names(names):
    validated_names = validate_names(names)
    upper_unique_names = sorted(set(validated_names), key=lambda x: x.upper(), reverse=True)
    return upper_unique_names

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))