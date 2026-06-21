class ListAccessor:
    DEFAULT_LIST = [10, 20, 30, 40, 50]

    @staticmethod
    def get_element_at_position(lst, position):
        try:
            return lst[position]
        except IndexError:
            raise ValueError("Index out of range")

    @staticmethod
    def test_get_element_at_position():
        assert ListAccessor.get_element_at_position([1, 2, 3, 4, 5], 2) == 3
        assert ListAccessor.get_element_at_position([1, 2, 3, 4, 5], 0) == 1
        assert ListAccessor.get_element_at_position([1, 2, 3, 4, 5], 4) == 5
        assert ListAccessor.get_element_at_position([1, 2, 3, 4, 5], -1) == 5
        try:
            ListAccessor.get_element_at_position([1, 2, 3, 4, 5], 5)
        except ValueError as e:
            assert str(e) == "Index out of range"
        try:
            ListAccessor.get_element_at_position([1, 2, 3, 4, 5], -6)
        except ValueError as e:
            assert str(e) == "Index out of range"

if __name__ == '__main__':
    ListAccessor.test_get_element_at_position()
    try:
        result = ListAccessor.get_element_at_position(ListAccessor.DEFAULT_LIST, 2)
        print(result)
    except ValueError as e:
        print(e)