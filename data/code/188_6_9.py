def reverse_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    reversed_gen = reverse_generator(sample_list)
    for item in reversed_gen:
        print(item)