class ListComparator:
    def compare_elements(self, list1, list2):
        if not (isinstance(list1, list) and isinstance(list2, list)):
            return "Both inputs must be lists"
        
        for index in range(min(len(list1), len(list2))):
            val1 = list1[index]
            val2 = list2[index]
            if val1 > val2:
                print(f"List 1 element {val1} is greater than List 2 element {val2}")

if __name__ == '__main__':
    comparator = ListComparator()
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 30, 50]
    comparator.compare_elements(list_a, list_b)