from collections import Counter

def count_occurrences(data_list):
    return dict(Counter(data_list))

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    occurrences = count_occurrences(sample_list)
    print(f"Occurrences of each element in {sample_list}: {occurrences}")