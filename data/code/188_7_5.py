from typing import List, Any

class ListReverser:
    def reverse_list_strict(self, input_list: List[Any]) -> List[Any]:
        return input_list[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 'a', 'b', 'c']
    reversed_list = reverser.reverse_list_strict(sample_list)
    print(reversed_list)