class Finder:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_final_index(self, target_item):
        last_index = -1
        for index, item in enumerate(self.data_list):
            if item == target_item:
                last_index = index
        return last_index

if __name__ == '__main__':
    finder_instance = Finder([1, 2, 3, 2, 4, 2, 5])
    target1 = 2
    result1 = finder_instance.find_final_index(target1)
    print(f"List: {finder_instance.data_list}, Target: {target1}, Final Index: {result1}")

    finder_instance.data_list = ['a', 'b', 'c', 'b', 'd', 'b']
    target2 = 'b'
    result2 = finder_instance.find_final_index(target2)
    print(f"List: {finder_instance.data_list}, Target: {target2}, Final Index: {result2}")

    finder_instance.data_list = [10, 20, 30, 40]
    target3 = 5
    result3 = finder_instance.find_final_index(target3)
    print(f"List: {finder_instance.data_list}, Target: {target3}, Final Index: {result3}")