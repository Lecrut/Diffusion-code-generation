UPPERCASE_SET = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

def process_names(names):
    upper_unique_names = sorted({name.upper() for name in names}, reverse=True)
    return [name for name in upper_unique_names if all(char in UPPERCASE_SET for char in name)]

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))