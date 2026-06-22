def reverse_iter(lst):
    for item in reversed(lst):
        yield item

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    for value in reverse_iter(sample_values):
        print(value)