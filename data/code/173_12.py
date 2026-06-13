class DataGrouper:
    def group_data(self, data):
        even_numbers = []
        odd_numbers = []
        for item in data:
            if isinstance(item, int):
                if item % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
        return {"even": even_numbers, "odd": odd_numbers}
if __name__ == '__main__':
    grouper = DataGrouper()
    sample_data = [1, 2, 3, 4, 5, 6, 'a', 7, 8, 'b']
    result = grouper.group_data(sample_data)
    print(result)