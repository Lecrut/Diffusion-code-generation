def count_names(names):
    from collections import Counter
    return Counter(names).most_common()

if __name__ == '__main__':
    sample_names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice']
    print(count_names(sample_names))