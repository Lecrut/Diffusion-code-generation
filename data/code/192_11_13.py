class ListIntersector:
    @staticmethod
    def convert_to_set(lst):
        return set(lst)

    @staticmethod
    def find_intersection(set_a, set_b):
        return set_a.intersection(set_b)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 2, 5]
    list2 = [4, 5, 6, 2, 1]
    
    intersector = ListIntersector()
    set_a = intersector.convert_to_set(list1)
    set_b = intersector.convert_to_set(list2)
    intersection = intersector.find_intersection(set_a, set_b)
    
    print(list(intersection))