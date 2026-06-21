from typing import List, Any

class ListReverser:
    def __init__(self):
        self.data = []

    def add_item(self, item: Any) -> None:
        self.data.append(item)

    def reverse_list_strict(self) -> List[Any]:
        return self.data[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    for item in [1, 2, 3, 'a', 'b', 'c']:
        reverser.add_item(item)
    
    reversed_list = reverser.reverse_list_strict()
    print(reversed_list)