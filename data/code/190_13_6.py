class ListValidator:
    def __init__(self, data):
        self._data = list(data)

    @staticmethod
    def check_element(target, lst):
        return target in lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    validator = ListValidator(sample_list)
    item1 = 3
    item2 = 6
    print(f"Does the list contain {item1}? {validator.check_element(item1, sample_list)}")
    print(f"Does the list contain {item2}? {validator.check_element(item2, sample_list)}")