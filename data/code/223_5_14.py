def max_element(lst):
    return max(lst, key=lambda x: (isinstance(x, int), x))

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, '7', 8]
    print(max_element(sample_values))