def find_violations(lst):
    return [lst[i] for i in range(1, len(lst)) if lst[i] < lst[i - 1]]

if __name__ == '__main__':
    sample_list = [1.0, 2.5, 3.3, 4.8, 5.9, 5.7, 6.0]
    result = find_violations(sample_list)
    print(result)