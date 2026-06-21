UPPERCASE_SET = set()

def process_names(names):
    global UPPERCASE_SET
    UPPERCASE_SET.update(name.upper() for name in names)
    return sorted(UPPERCASE_SET, reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'alice', 'Bob']
    print(process_names(sample_names))