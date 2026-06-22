class ListProcessor:
    def get_last_item(self, lst):
        if not lst:
            raise IndexError("list index out of range")
        return lst[-1]

if __name__ == '__main__':
    processor = ListProcessor()
    sample_list = [1, 2, 3, 4, 5]
    result = processor.get_last_item(sample_list)
    print(result)