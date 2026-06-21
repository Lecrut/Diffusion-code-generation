def process_names(names):
    name_map = {'A': 'Alice', 'B': 'Bob', 'C': 'Charlie'}
    upper_unique_names = sorted(set(name.upper() for name in names), reverse=True)
    return [name_map.get(name[0], name) for name in upper_unique_names]

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))