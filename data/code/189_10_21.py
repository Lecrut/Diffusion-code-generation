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
    modifier = ListModifier([10, 20, 30, 40, 50, 20])
    modified_list_1 = modifier.remove_element(20)
    print(modified_list_1)

    modifier.lst = [15, 25, 35, 45, 25, 55]
    modified_list_2 = modifier.remove_element(25)
    print(modified_list_2)