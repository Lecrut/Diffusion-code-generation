from typing import List

class ElementFinder:
    def __init__(self, list1: List[str], list2: List[str]):
        self.set1 = set(item.lower() for item in list1)
        self.set2 = set(item.lower() for item in list2)

    def find_common(self) -> List[str]:
        common = self.set1.intersection(self.set2)
        return sorted([item.capitalize() for item in common])

if __name__ == '__main__':
    finder = ElementFinder(["Apple", "Banana", "Cherry", "Date"], ["apple", "Elderberry", "Banana", "Fig"])
    common_items = finder.find_common()
    print(common_items)