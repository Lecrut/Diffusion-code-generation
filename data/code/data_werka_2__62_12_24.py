class ListElementFetcher:
    @staticmethod
    def fetch_second_element(lst):
        if len(lst) < 2:
            return None
        return lst[1]

if __name__ == '__main__':
    my_list = [10, 20, 30, 40]
    second_element = ListElementFetcher.fetch_second_element(my_list)
    print(second_element)

    # Additional test cases
    short_list = [5, 15]
    single_element_list = [7]
    empty_list = []
    print(ListElementFetcher.fetch_second_element(short_list))        # Should print 15
    print(ListElementFetcher.fetch_second_element(single_element_list))  # Should print None
    print(ListElementFetcher.fetch_second_element(empty_list))         # Should print None