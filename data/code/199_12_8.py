def sort_names(names):
    return sorted(names, key=lambda name: name.lower())

if __name__ == '__main__':
    sample_names = ['Alice', 'bob', 'Charlie', 'dave']
    print(sort_names(sample_names))