from typing import List

class CommonElementsFinder:
    def find_common_elements(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = {item.lower() for item in list1}
        set2 = {item.lower() for item in list2}
        common = set1.intersection(set2)
        return sorted([item.capitalize() for item in common])

if __name__ == '__main__':
    finder = CommonElementsFinder()
    list_a = ["Apple", "Banana", "Cherry", "Date"]
    list_b = ["apple", "Elderberry", "Banana", "Fig"]
    common_items = finder.find_common_elements(list_a, list_b)
    print(common_items)