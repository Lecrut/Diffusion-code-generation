def reverse_generator(lst):
    start = 0
    end = len(lst) - 1
    while start <= end:
        yield lst[end]
        end -= 1

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    for item in reverse_generator(sample_list):
        print(item)