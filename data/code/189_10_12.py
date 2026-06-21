class ListModifier:
    def __init__(self, initial_list):
        self.list = initial_list

    def remove_element(self, element):
        result = []
        for item in self.list:
            if item != element:
                result.append(item)
        return result

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500, 200]
    modifier = ListModifier(sample_list)
    modified_list = modifier.remove_element(200)
    print(modified_list)