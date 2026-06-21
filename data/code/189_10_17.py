class ListModifier:
    def __init__(self, lst):
        self.lst = lst

    def remove_element(self, element):
        result = []
        for item in self.lst:
            if item != element:
                result.append(item)
        return result

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 20]
    modifier = ListModifier(sample_list)
    modified_list = modifier.remove_element(20)
    print(modified_list)