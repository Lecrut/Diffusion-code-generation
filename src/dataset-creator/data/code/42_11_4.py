from typing import Iterable, List
def sort_strings(collection: Iterable[str]) -> List[str]:
    return sorted(list(collection))
if __name__ == '__main__':
    sample_data = ["banana", "apple", "cherry", "date", "elderberry"]
    result = sort_strings(sample_data)
    print(result)