class ListUtils:
    @staticmethod
    def get_first_element(data):
        return data[0] if data else None

if __name__ == '__main__':
    my_list = [5, 15, 25, 35]
    first = ListUtils.get_first_element(my_list)
    print(first)