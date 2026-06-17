import sys
def find_middle_index(iterable):
    try:
        iterator = iter(iterable)
        length = 0
        if hasattr(iterable, '__len__'):
            length = len(iterable)
        else:
            temp_list = list(iterator)
            length = len(temp_list)
        middle_index = length // 2
    except Exception as e:
        raise ValueError(f"Error calculating index: {e}")
if __name__ == '__main__':
    data1 = [0, 1, 2, 3, 4]
    def generator():
        for i in range(5):
            yield i
    result_list = find_middle_index(data1)
    result_gen = find_middle_index(generator())
    print(f"List middle index: {result_list}")
    print(f"Generator middle index: {result_gen}")