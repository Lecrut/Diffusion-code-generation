class DynamicList:

    def __init__(self):
        self._data = []

    def append(self, item):
        self._data.append(item)

    def get_by_position(self, position):
        if position < 0 or position >= len(self._data):
            raise ValueError('Position out of range')
        return self._data[position]
if __name__ == '__main__':
    dynamic_list = DynamicList()
    dynamic_list.append(10)
    dynamic_list.append(20)
    dynamic_list.append(30)
    try:
        print(dynamic_list.get_by_position(1))
    except ValueError as e:
        print(e)