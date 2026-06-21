from typing import List, Any

def reverse_list_strict(lst: List[Any]) -> List[Any]:
    return lst[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 'a', 'b', 'c']
    print(reverse_list_strict(sample))