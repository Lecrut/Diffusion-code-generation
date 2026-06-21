def process_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All elements in the input list must be strings.")
    
    upper_unique_names = sorted(set(name.upper() for name in names), reverse=True)
    return upper_unique_names

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    try:
        print(process_names(sample_names))
    except ValueError as e:
        print(e)