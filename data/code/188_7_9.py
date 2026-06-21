from typing import List, Any

class ListReverser:
    @staticmethod
    def reverse_list_strict(input_list: List[Any]) -> List[Any]:
        return input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 'a', 'b', 'c']
    reversed_list = ListReverser.reverse_list_strict(sample_list)
    print(reversed_list)