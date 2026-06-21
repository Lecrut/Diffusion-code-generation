def reverse_generator(lst):
    for i in range(len(lst) - 1, -1, -1):
        yield lst[i]

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    for item in reverse_generator(sample_list):
        print(item)