def process_names(names):
    return sorted(set(name.upper() for name in names), reverse=True)

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'dave', 'Alice']
    print(process_names(sample_names))