class ListCounter:
    def count_occurrences(self, data_list, item):
        count = 0
        for element in data_list:
            if element == item:
                count += 1
        return count
if __name__ == '__main__':
    counter = ListCounter()
    list1 = [1, 2, 3, 2, 4, 2, 5]
    item1 = 2
    result1 = counter.count_occurrences(list1, item1)
    print(f"List: {list1}, Item: {item1}, Count: {result1}")
    list2 = ['a', 'b', 'c', 'd']
    item2 = 'z'
    result2 = counter.count_occurrences(list2, item2)
    print(f"List: {list2}, Item: {item2}, Count: {result2}")
    list3 = [10, 20, 10, 30, 10]
    item3 = 10
    result3 = counter.count_occurrences(list3, item3)
    print(f"List: {list3}, Item: {item3}, Count: {result3}")