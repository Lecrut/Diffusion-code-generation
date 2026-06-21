def reverse_using_iter(lst):
    return list(reversed(lst))

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reversed_values = reverse_using_iter(sample_values)
    print(reversed_values)