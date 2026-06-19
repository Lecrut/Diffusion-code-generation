class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_last_occurrence_index(self, item):
        last_index = -1
        for i in range(len(self.data) - 1, -1, -1):
            if self.data[i] == item:
                last_index = i
                break
        return last_index

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 5, 3]
    analyzer1 = ListAnalyzer(list1)
    item1 = 5
    result1 = analyzer1.find_last_occurrence_index(item1)
    print(f"List: {list1}, Item: {item1}, Last Index: {result1}")

    list2 = ['a', 'b', 'c', 'a', 'd', 'a']
    analyzer2 = ListAnalyzer(list2)
    item2 = 'a'
    result2 = analyzer2.find_last_occurrence_index(item2)
    print(f"List: {list2}, Item: {item2}, Last Index: {result2}")

    list3 = [10, 20, 30]
    analyzer3 = ListAnalyzer(list3)
    item3 = 5
    result3 = analyzer3.find_last_occurrence_index(item3)
    print(f"List: {list3}, Item: {item3}, Last Index: {result3}")